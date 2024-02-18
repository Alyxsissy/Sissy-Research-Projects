REM Cleanup Windows driver cache

@echo off
for /L %%A in (1,1,300) do (
echo Deleting OEM%%A.INF
pnputil /d OEM%%A.INF
)