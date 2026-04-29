REM learning for in operator
REM @ECHO OFF

REM encoding utf-8
chcp 65001

set Variable=test

REM for cycle with files (in variable put only one character)
for %f in (./*) do @echo %f
REM print filename without extansion
for %f in (./*) do @echo %~nf

REM for cycle with directory
for /D %d in (.\*) do @echo %~nd

REM for cycle recursion working with files and directories
for /R .\ %r in (*) do @echo %r


REM 
cmd /d