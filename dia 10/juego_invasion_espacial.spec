# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['juego_invasion_espacial.py'],
    pathex=[],
    binaries=[],
    datas=[('ovni.png', '.'), ('fondo.jpg', '.'), ('cohete.png', '.'), ('enemigo.png', '.'), ('bala.png', '.'), ('disparo.mp3', '.'), ('Golpe.mp3', '.'), ('MusicaFondo.mp3', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='juego_invasion_espacial',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
