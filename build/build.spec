# -*- mode: python -*-
from PyInstaller.utils.hooks import collect_all

block_cipher = None

# Configurações para Flask e ReportLab
datas, binaries, hiddenimports = collect_all('flask')
rl_datas, rl_binaries, rl_hiddenimports = collect_all('reportlab')

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=binaries + rl_binaries,
    datas=datas + rl_datas + [
        ('templates/*', 'templates'),
        ('static/*', 'static'),
        ('database.db', '.')
    ],
    hiddenimports=hiddenimports + rl_hiddenimports + [
        'flask', 'werkzeug', 'jinja2', 'itsdangerous', 'click',
        'sqlite3', 'pandas', 'fpdf', 'xhtml2pdf',
        'reportlab', 'reportlab.graphics.barcode.code128',
        'reportlab.graphics.barcode.code39',
        'reportlab.graphics.barcode.common'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)

exe = EXE(
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='BibliotecaApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False
)