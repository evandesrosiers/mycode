#!/usr/bin/env python3
"""Alta3 Research || Author RZFeeser@alta3.com
Learning how to use functions"""

## Installs the crayons package.
## python3 -m pip install crayons
## import statements ALWAYS go up top
import crayons

def main():
    """Runtime code. Always indent a function"""
    # print 'red string' in red


    print('{} Sean {}'.format(crayons.cyan('Evan'), crayons.yellow('DesRosiers')))

# we must call our main function or our code will not run!
main()

