@ECHO OFF
pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
    set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=docs\source
set BUILDDIR=docs\build

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
