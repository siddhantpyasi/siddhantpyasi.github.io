---
layout: post
title: "Regex Tutorial - Pt 1"
date: 2017-07-19 01:00:00 -0400
tags: programming
heading-bg-color: "#ff4500"
heading-bg-text: "#fff"
---

Regular Expressions are a really useful tool, that can shorten your work by 6-7 hours (if you know how to use them), or can end with you abandoning the project altogether in total frustration. To the newcomer, they may appear daunting - here's my attempt to make them less so.

I am going to address Regexes in [MATLAB](https://www.mathworks.com/products/matlab.html). Before going into the MATLAB specific functions, however, here are some common metacharacters used in regular expressions.

|	Metacharacter		|								Meaning							|
|	:------------- :|:--------------------------------: |
|				.					|							Any character					|
|				[]				| Any character within the brackets	|
|				[^]				|	Any character not in brackets			|
|				\w				| A word character [a-zA-Z0-9]			|
|				\W				| Not a word character [^a-zA-Z0-9]	|
|				\d				|						A digit [0-9]						|
|				\D				|					Not a digit [^0-9]				|
|				\s				|					Whitespace [\t\r\n\f\v]		|				
|				\S				|			Not whitespace [^\t\r\n\f\v]	|
|				+					|			Match one or more occurrences	|
|				*					|	Match zero or more occurrences (greedy matching)	|
|				?					|		Match zero or one occurrence		|
|				{n, m}		|		Match between n and m occurrences		|
|									|																		|

			
#### Normal Matching
Let's now use these metacharacters to get something done using regexes.

We have the following emails that we need to extract domain names from:
```matlab
get_domain_names_from_these = ['siddhantpyasi@yahoo.com '...
'bill@gates.com '...
'el__cid@castille.com']
```

For this, we need to write a regular expression, that captures the letters after the '@' symbol. Look at the letters present there.
After the @ symbol, we have some letters(\w+), a full stop(escape a full stop using a backward slash, like so: \\.), then some other letters(\w+).
Just put those three sets of metacharacters together, and voila! You have your first regular expression!
```matlab
reg_expr = '\w+\.\w+'
```

Now that we've written a regular expression, let's use a MATLAB function to put it to use. We'll use the function _regexp_ from the MATLAB standard library. Because we're looking for bits of text that **match** the regex we wrote, we're gonna write the function this way:
```matlab
matched_bits = regexp(get_domain_names_from_these, reg_expr, 'match')
``` 
The function takes in the string to be matched, the regex and the action that you want MATLAB to perform - in this case, match the regex.

Here's the result in MATLAB 2017a:
![Regex Result](assets/img/matlab_regex_match.png){: .size-small}

Here's another example. We have a string containing names of Hollywood stars:
```matlab
string2 = 'Jennifer Lawrence, Matthew McConaughey, Jennifer Hudson, Robert Downey Jr, Jen Aniston, Jude Law, Jennifer Lopez';
```

Let's find all the 'Jennifer\'s'. If you see, some are 'Jen\'s', while some are 'Jennifer\'s'. We need to write something that gets both kinds.
They all have 'Je' at the beginning, so we put that in the regex. After that, they have one or more letters (\w+), a whitespace (\s) and their surnames (\w+). Put it all together, and you get this:
```matlab
reg_expr = 'Je\w+\s\w+'
```

Here's the result:
![Regex Result](assets/img/matlab_regex_match2.png){: .size-small}

Some XKCD to show you a scenario where knowledge of regexes shall save the day
![XKCD Regex](assets/img/xkcd_regex.png){: .size-small}

Part 1 of the tutorial ends here. Part 2 is still under construction, will let you know once its done!