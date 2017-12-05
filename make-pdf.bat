rem make pdf from json and tex

set "name=schedule"

if {%1} == {} (set "obj=makepdf") ^
else (set "obj=%1")

call :%obj% %name%
goto :eof

:makepdf
python json2tex.py
latexmk -xelatex -synctex=-1  -src-specials -interaction=nonstopmode "%1.tex"
pause
goto :eof

:innerdel
set "suffix=%2"
for %%i in %2 do if exist %1.%%i (del %1.%%i)
goto :eof

:clear
set "suffix=(fdb_latexmk, aux, fls, log, out, toc, synctex, xdv)"
for %%i in %suffix% do if exist %1.%%i (del %1.%%i)
goto :eof

:clearall
call :clear %1
if exist %1.pdf (del %1.pdf)
if exist reports.tex (del reports.tex)
if exist table.tex (del table.tex)
goto :eof