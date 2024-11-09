import os
import subprocess
import shutil

def build_executable():
    # Ensure we're in the project root directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Create a build directory if it doesn't exist
    if not os.path.exists('build'):
        os.makedirs('build')

    # Run PyInstaller
    subprocess.call([
        'pyinstaller',
        '--name=KaryotypeAnalyzer',
        '--windowed',
        '--onefile',
        '--add-data=src;src',
        'src/main.py'
    ])

    # Copy the resulting executable to the build directory
    shutil.copy('dist/KaryotypeAnalyzer.exe', 'build/KaryotypeAnalyzer.exe')

    print("Build complete. Executable is in the 'build' directory.")

if __name__ == "__main__":
    build_executable()
