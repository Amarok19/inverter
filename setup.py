from cx_Freeze import setup, Executable

VERSION = "1.0.1"

# include_files = [
#     ('my/path', 'target/path'),
#     ('my/path', 'target/path'),
# ]

# build_options = dict(
#     packages=['gi', 'packaging', 'pikepdf'],
#     excludes=['tkinter', 'test'],
#     # manually added to the lib folder
#     bin_excludes=['zlib1.dll'],
#     include_files=include_files,
# )

msi_options = dict(
    target_name=f'Inverter-{VERSION.replace(".", "_")}.msi',
    upgrade_code='{70d1a014-69e6-4db3-a0e3-2c3da347c895}'  # Thanks https://www.guidgenerator.com/online-guid-generator.aspx!
)

setup(name='Inverter',
      version=VERSION,
      description='A simple utility that converts various .xml exports of batches of invoices to .epp files (EDI++ structure).',
      # options=dict(bdist_msi=msi_options),
      # cmdclass={'bdist_zip': bdist_zip},
      executables=[Executable('inverter.pyw',
                              base='Win32GUI',
                              targetName='inverter.exe',
                              icon='assets/inverter.ico',
                              shortcutName='Inverter',
                              shortcutDir='StartMenuFolder'
                              )])
