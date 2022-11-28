# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(
    ["tk_1.py"],
    pathex=[
        "C:\\Users\\33612\\Documents\\projets\\formations\\organismes\\oh_ce_cours\\vibratec_octobre_2020\\cours\\tape_en_cours\\templating_gui"
    ],
    binaries=[],
    datas=[],  ##("C:\\Users\\33612\\Documents\\projets\\formations\\organismes\\oh_ce_cours\\vibratec_octobre_2020\\cours\\tape_en_cours\\templating_gui\\window_handle_templating.ui", ".")],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="TestTk",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)
