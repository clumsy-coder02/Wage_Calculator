# Wage Calculator

A simple Python command-line tool to calculate your earnings based on working hours and hourly rate.

## Description

The Wage Calculator helps you quickly determine how much you earned during a work shift. Simply provide your start time, end time, and hourly rate, and the program will calculate your total earnings.

## Features

- Easy-to-use command-line interface
- Supports time input in hours and minutes
- Automatically handles minute-to-hour conversions
- Displays work summary with formatted times and payment information

## Requirements

- Python 3.x

## Usage

1. Run the program:

   ```bash
   python main.py or python3 main.py
   ```

2. Enter the requested information when prompted:
   - **Starting hour**: The hour you started work (24-hour format)
   - **Starting minutes**: The minutes you started work
   - **Stopping hour**: The hour you finished work
   - **Stopping minutes**: The minutes you finished work
   - **Hourly rate**: Your hourly wage (in dollars)

3. The program will display:
   - Your work time range
   - Total hours worked
   - Your hourly rate
   - Total payment earned

## Example

```markdown
Hourly Wage Calculator:

Enter starting hour: 9
Enter starting minutes: 30
Enter stopping hour: 17
Enter stopping minutes: 45
Enter your hourly rate: 25

Worked from 09:30 to 17:45
Total working hours: 8 hrs
Your hourly rate: $25
Payment: $200
```

## How It Works

The calculator computes working hours by:

1. Taking the difference between end and start minutes
2. Converting any minutes ≥ 60 to additional hours
3. Adding these to the hour difference
4. Multiplying total hours by the hourly rate

## Notes

- Times should be entered in 24-hour format
- The hourly rate should be entered as an integer (whole number)
- Fractional hour calculations are rounded down to whole hours

## License

This project is open source and available for personal use.
