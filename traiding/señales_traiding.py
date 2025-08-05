import yfinance as yf
import pandas as pd
import mplfinance as mpf
import ta
import sys
from os import system


# --- Función para detectar patrones de velas ---
def detectar_patron(row):
    cuerpo = abs(row['Close'] - row['Open'])
    sombra_sup = row['High'] - max(row['Close'], row['Open'])
    sombra_inf = min(row['Close'], row['Open']) - row['Low']

    if cuerpo < sombra_inf * 0.3 and sombra_sup < cuerpo * 0.5:
        return 'Martillo'
    elif cuerpo < sombra_sup * 0.3 and sombra_inf < cuerpo * 0.5:
        return 'Martillo Invertido'
    elif row['Close'] > row['Open'] and row['Close'] > row['High'] - cuerpo * 0.2:
        return 'Envolvente Alcista'
    elif row['Close'] < row['Open'] and row['Close'] < row['Low'] + cuerpo * 0.2:
        return 'Envolvente Bajista'
    else:
        return ''


# --- Menú interactivo ---
system('cls')
print("📈 LECTOR DE VELAS CON SEÑALES DE COMPRA/VENTA\n")

ticker = input("🔹 Ticker (ej: AAPL, MSFT, TSLA, EC): ").upper()
start_date = input("🔹 Fecha de inicio (YYYY-MM-DD): ") or '2024-01-01'
end_date = input("🔹 Fecha de fin (YYYY-MM-DD): ") or '2024-12-31'

print("\n📥 Descargando datos...")
df = yf.download(ticker, start=start_date, end=end_date, interval='1d')

# --- Validar datos descargados ---
if df.empty:
    print("❌ No se encontraron datos para ese ticker o rango de fechas.")
    sys.exit()

df.dropna(inplace=True)
df = df[df['Close'].notna()]

# --- Cálculo de indicadores ---
try:
    df['RSI'] = ta.momentum.RSIIndicator(close=df['Close']).rsi()
    df['MACD'] = ta.trend.MACD(close=df['Close']).macd()
    df['SMA20'] = ta.trend.SMAIndicator(close=df['Close'], window=20).sma_indicator()
    df['SMA50'] = ta.trend.SMAIndicator(close=df['Close'], window=50).sma_indicator()
except Exception as e:
    print(f"⚠️ Error al calcular indicadores técnicos: {e}")
    sys.exit()

# --- Detectar patrones de velas ---
df['Patron'] = df.apply(detectar_patron, axis=1)

# --- Generar señales de compra/venta ---
df['Señal'] = ''

for i in range(1, len(df)):
    señales = []

    # RSI
    if df['RSI'].iloc[i] < 30:
        señales.append('Compra (RSI)')
    elif df['RSI'].iloc[i] > 70:
        señales.append('Venta (RSI)')

    # Cruce de medias móviles
    if df['SMA20'].iloc[i - 1] < df['SMA50'].iloc[i - 1] and df['SMA20'].iloc[i] > df['SMA50'].iloc[i]:
        señales.append('Compra (SMA)')
    elif df['SMA20'].iloc[i - 1] > df['SMA50'].iloc[i - 1] and df['SMA20'].iloc[i] < df['SMA50'].iloc[i]:
        señales.append('Venta (SMA)')

    # Patrones de velas
    patron = df['Patron'].iloc[i]
    if patron in ['Martillo', 'Envolvente Alcista']:
        señales.append('Compra (Patrón)')
    elif patron in ['Martillo Invertido', 'Envolvente Bajista']:
        señales.append('Venta (Patrón)')

    df.iat[i, df.columns.get_loc('Señal')] = ' | '.join(señales)

# --- Mostrar últimas señales ---
ultimas = df[df['Señal'] != ''].tail(10)[['Close', 'RSI', 'SMA20', 'SMA50', 'Patron', 'Señal']]
print("\n📌 Últimas señales de compra/venta detectadas:")
print(ultimas.to_string())

# --- Crear gráficos con indicadores ---
apds = [
    mpf.make_addplot(df['SMA20'], color='blue'),
    mpf.make_addplot(df['SMA50'], color='orange'),
    mpf.make_addplot(df['RSI'], panel=1, color='purple', ylabel='RSI'),
    mpf.make_addplot(df['MACD'], panel=2, color='green', ylabel='MACD'),
]

print("\n📊 Mostrando gráfico...")
mpf.plot(
    df,
    type='candle',
    style='charles',
    title=f'Gráfico de Velas - {ticker}',
    volume=True,
    addplot=apds,
    panel_ratios=(3, 1, 1),
    figratio=(16, 9),
    figscale=1.2
)