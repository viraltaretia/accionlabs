"""
Problem Statement: https://pastebin.com/qrnX9Y4G
Author: Viral Taretia
"""

import re
import sys


num_count = "0"
prev_num_char = "*"
len_prev_char = len(prev_num_char)
prev_line = ""
indent_count = " "
star_pat = "^\*+\s+"
dot_pat = "^\.+\s+"


def process_line(p_line, cur_line):
    """This function prevents need to seek forward in file by
    managing previous line buffer.
    Args:
        p_line: Previous line
        cur_line: Current line in file pointer
    Returns:
        None
    """
    global num_count
    global prev_num_char
    global len_prev_char
    global indent_count
    global star_pat
    global dot_pat

    if not p_line:
        return
    else:
        first_char = p_line.split()[0]
        if re.match("\*+", first_char):
            cur_char = first_char
            if cur_char == prev_num_char:
                if len_prev_char == 1:
                    num_count = str(int(num_count) + 1)
                else:
                    num_count = num_count[:-1] + str(int(num_count[-1]) + 1)
            elif len(cur_char) > len_prev_char:
                num_count = num_count + ".1"
            else:
                diff = len_prev_char - len(cur_char)
                d = -(diff * 2)
                tmp_num = num_count[:d]
                num_count = tmp_num[:-1] + str(int(tmp_num[-1]) + 1)

            len_prev_char = len(cur_char)
            prev_num_char = cur_char

            print re.sub(star_pat, "%s " % num_count, p_line)

        elif re.match("\.+", first_char):
            sub_char = "-"
            cur_char = first_char
            next_line = cur_line
            next_char = next_line.split()[0]
            if re.match("\*+", next_char):
                print re.sub(
                    dot_pat, indent_count + "%s " % sub_char, p_line)
                indent_count = " "
            elif re.match("\.+", next_char):
                if len(next_char) > len(cur_char):
                    print re.sub(dot_pat, indent_count + "+ ", p_line)
                    indent_count += " "
                else:
                    print re.sub(
                        dot_pat, indent_count + "%s " % sub_char, p_line)
            else:
                """For multi line subtext"""
                print re.sub(
                    dot_pat, indent_count + "%s " % sub_char, p_line)
        else:
            """For multi line sub text"""
            print p_line


for line in sys.stdin:
    """in case of empty lines avoid processing"""
    if line.strip() == "":
        continue

    process_line(prev_line, line)
    prev_line = line

"""For Handling last line"""
first_char = prev_line.split()[0]
if re.match("\.+", first_char):
    print re.sub(dot_pat, indent_count + "- ", prev_line)
elif re.match("\*+", first_char):
    print re.sub(star_pat, "%s " % num_count, prev_line)
