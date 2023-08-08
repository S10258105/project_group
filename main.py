from pathlib import Path

file_path = Path(r"C:\project_group\summary_report.txt")
file_path.touch()

import cash_on_hand, profit_loss, overheads

with file_path.open(mode="w", encoding="UTF-8") as file:

    overheads_output = overheads.overheads_function()
    cash_output = cash_on_hand.cash_function()
    profit_output = profit_loss.profit_function()
    
    file.write(overheads_output)
    file.write(cash_output)
    file.write(profit_output)



