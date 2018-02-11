from string import Template
from routines.routines import *
from config.config import *

"""
Generates a spreadsheet from a log file. 
"""

source = open(log_file, 'r', encoding="utf8")

destination = open(output_file, 'w')

template = build_template_string()

# Write file header
destination.write(template.replace('$', ''))

template = Template(template)

for line in source:
    dataForLine = {}
    for var, routine in dataToLog.items():
        dataForLine[var] = routine.operation(line)

    for key, data in dataForLine.items():
        # Time Stamp handling is hardcoded in.
        if data != '' and key != 'Time_Stamp':
            destination.write(
                template.substitute(dataForLine)
            )
            break

source.close()
destination.close()
