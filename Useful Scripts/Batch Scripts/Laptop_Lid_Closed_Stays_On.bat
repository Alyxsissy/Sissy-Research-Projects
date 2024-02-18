REM Do nothing when you close the lid of your laptop.

powercfg /setacvalueindex scheme_current sub_buttons lidaction 0
powercfg /setdcvalueindex scheme_current sub_buttons lidaction 0

REM Re-activate current scheme to make settings take effect immediately.
powercfg /setactive scheme_current