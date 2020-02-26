---
layout: post
title: "Random Portfolio Generator"
date: 2017-09-17 15:00:00 -0400
tags: finance
heading-bg-color: "#fff000"
heading-bg-text: "000000"
---
I'm taking Finance 3301 - Investments, under Professor [Gary Porter](http://www.damore-mckim.northeastern.edu/faculty/p/porter-gary) this semester. The first project that we did for the class required us to create a random portfolio.

We had to randomly select a stock exchange, and then randomly pick five stocks from that exchange. I decided to write a script in Ruby that would do that for me. I got a CSV file of stocks in different exchanges from the NASDAQ FTP server. Then I just wrote the script, which used the random number generator like there's no tomorrow.

The code can be found [here](https://github.com/siddhantpyasi/RandomPortfolio).

These were the stocks picked for me by the generator:
![Stocks](/assets/img/Stocks.png){: .size-small}

__UPDATE:__ I sold the portfolio on the 1st of December, and got a return of
9.060%, while the NASDAQ grew 5.997%.
