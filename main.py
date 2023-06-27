#!/usr/bin/python3

import sys;
import signal;
import time;

################################################################################

def SignalHandler(signum, frame):
  print("\nSIGINT!");
  exit(0);

################################################################################

def PrintRules(rules, rulesList):
  # 111	110	101	100	011	010	001	000
  visual = [ "###", "##.", "#.#", "#..",
             ".##", ".#.", "..#", "..."];

  print(f"Current ruleset is { rules }:\n");

  output = "";

  for item in visual:
    output += f"{ item } | ";

  output += "\n";

  cnt = 0;
  for i in range(0, 32, 4):
    output += " ." if rulesList[cnt] == 0 else " #";
    output += "  | ";

    cnt += 1;

  output += "\n";

  print(output);

################################################################################

def PrintStart(start, gen1):

  print(f"Starting configuration is { start }:\n");

  for item in gen1:
    if item == 0:
      print(".", end="");
    else:
      print("#", end="");

  print("\n\n");

################################################################################

def PrintGen(gen):
  for item in gen:
    if item == 0:
      print(".", end="");
    else:
      print("#", end="");

  print("");

################################################################################

def main():
  #
  # Implementation of so-called Elementary Cellular Automaton.
  # It's a line where every cell's status is determined by its two neighbours:
  #
  # LCR
  #  N
  #
  # Where C - current cell,
  # L - left neighbour,
  # R - right neighbour,
  # N - new cell, what the result shall be on the next generation.
  #
  # Since every cell is determined by two neighbours, there are maximum of 2^8
  # possible rules of production.
  #
  if len(sys.argv) < 5:
    print(f"Usage: { sys.argv[0] } <RULE> <OUTPUT_LENGTH> <DELAY_MS> <WRAP> [<START>]");
    print("");
    print("<RULE> - decimal number representing binary mask of production rules:");
    print("");
    print("         ### | ##. | #.# | #.. | .## | .#. | ..# | ...");
    print("          0     0     0     0     0     0     0     0");
    print("");
    print("<OUTPUT_LENGTH> - how long the output should be in characters");
    print("<DELAY_MS>      - delay between next iteration of automaton");
    print("<WRAP>       - if negative do not wrap cells around when considering neighbours,");
    print("               otherwise 0 or 1 as bounds");
    print("");
    print("<START> - optional starting configuration bitmask as decimal number.");
    print("          If not specified, starting configuration will be one cell");
    print("          in the middle of the line with OUTPUT_LENGTH / 2.");
    print("");
    exit(0);

  signal.signal(signal.SIGINT, SignalHandler);

  rules = int(sys.argv[1]) % 256;

  noWrap = False;

  outLen = 80;
  delayMs = 0;

  outLen = int(sys.argv[2]);
  delayMs = int(sys.argv[3]);

  delayMs = delayMs / 1000;

  maxNum = pow(2, outLen) - 1;

  start = pow(2, outLen // 2);

  noWrap = False;
  wrapSymbol = int(sys.argv[4]);

  if wrapSymbol >= 0:
    noWrap = True;
    wrapSymbol = 0 if wrapSymbol == 0 else 1;

  if len(sys.argv) == 6:
    start = int(sys.argv[5]);

  if (start < 0):
    start = 0;

  if (start > maxNum):
    start = maxNum;

  #
  # Can't use spaces with format specifiers.
  #
  startStr = str(f"{start:b}");
  rulesStr = str(f"{rules:b}");

  lns = len(startStr);
  lnr = len(rulesStr);

  gen1 = [ 0 ] * outLen;
  gen2 = [ 0 ] * outLen;

  zero = [ 0 ] * outLen;

  for i in range(1, lns + 1):
    gen1[-i] = int(startStr[-i]);

  rulesList = [ 0, 0, 0, 0, 0, 0, 0, 0 ];

  upTo = min(lnr, 8);

  for i in range(1, upTo + 1):
    rulesList[-i] = int(rulesStr[-i]);

  PrintStart(start, gen1);
  PrintRules(rules, rulesList);

  PrintGen(gen1);

  while True:
    for i in range(0, outLen):
      if (i - 1) < 0:
        L = gen1[-1];
      else:
        L = gen1[i - 1] if noWrap == False else wrapSymbol;

      C = gen1[i];

      if (i + 1) <= outLen - 1:
        R = gen1[i + 1];
      else:
        R = gen1[0] if noWrap == False else wrapSymbol;

      ind = 7 - int(f"{ L }{ C }{ R }", 2);

      gen2[i] = rulesList[ind];

    PrintGen(gen2);

    gen1 = gen2.copy();
    gen2 = zero.copy();

    time.sleep(delayMs);

################################################################################

if __name__ == "__main__":
  main();
