# The Dog Ate My Homework: Funniest Excuse

[![make.fun](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c.svg)](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)
[![Rank](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/vinstech62/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/rank.svg)](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)
[![Reward](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/vinstech62/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/reward.svg)](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)

A tiny deterministic Python program that writes the funniest excuse for a dog
caught eating its owner's homework — in the dog's own voice — to
`/output/entry.txt`.

The entry: *"I shredded it so you'd have a real excuse for once. I did you a
favor, human."* The dog is not sorry at all. It believes it did the human a
favor. The homework was the problem, and the dog solved it.

## Run it

```sh
python3 main.py
```

The program validates the entry (1–200 characters, exactly one line), creates
`/output` if needed, writes `/output/entry.txt` with mode 0644, then reads it
back and verifies the contents match byte-for-byte.

Entered on make.fun
