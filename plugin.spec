# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['src/plugin.py'],
    pathex=["/root/infernet-spacecore"],
    binaries=[],
    datas=[("/root/miniconda/envs/infern/lib/python3.11/site-packages/pyfiglet/fonts/", "pyfiglet/fonts/")],
    hiddenimports=['rich', 'structlog', 'grpc', 'grpc_tools', 'grpc._cython', 'grpc._cython.cygrpc'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='plugin',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='plugin-i',
)