@echo off
rem make pdf from json and tex

set "name=schedule"

if {%1} == {} (set "obj=makepdf") else (set "obj=%1")

for %%i in (makepdf, py, tex, clean, cleanall) do  (
	if {%%i} == {%obj%} (
		call :%obj% %name%
		echo +---------------------------------------
		echo +  Command `%~n0 %obj%` is done!
		echo +---------------------------------------
		goto :end
		)
	)
@echo off
echo "Option must be one of `(makepdf, py, tex, clean, cleanall)`!!!"
echo "     The default option is makepdf."
echo "     For example: `./make-pdf`, `./make-pdf py`, `./make-pdf clean`."
:end
goto :eof

:makepdf
call :cleanall
call :py
call :tex %1
goto :eof

:py
call :require json
python json2tex.py
goto :eof

:tex
call :require tex
latexmk -xelatex -synctex=-1  -src-specials -interaction=nonstopmode "%1.tex"
goto :eof

:require
call :nonexist table.%1
call :nonexist reports.%1
goto :eof

:nonexist
if not exist %1 (call :echoexit)
goto :eof

:echoexit
echo "file: %1 non-exist!!! please run `./make-pdf py` or `./make-pdf`!!!"
pause
exit
goto :eof

:innerdel
set "suffix=%2"
for %%i in %2 do if exist %1.%%i (del %1.%%i)
goto :eof

:clean
set "suffix=(fdb_latexmk, aux, fls, log, out, toc, synctex, xdv)"
for %%i in %suffix% do if exist %1.%%i (del %1.%%i)
goto :eof

:cleanall
call :clean %1
call :cleanauto
if exist %1.pdf (del %1.pdf)
goto :eof

:cleanauto
if exist reports.tex (del reports.tex)
if exist table.tex (del table.tex)
goto :eof
