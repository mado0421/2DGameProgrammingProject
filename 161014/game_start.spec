# -*- mode: python -*-

block_cipher = None


a = Analysis(['game_start.py'],
             pathex=['C:\\2DGP\\2DGP\\161014'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='game_start',
          debug=False,
          strip=False,
          upx=True,
          console=True )
