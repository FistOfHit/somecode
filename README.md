# Some Code
Throwing together some code that I use pretty often at work, so I dont have to keep finding it and copy/pasting it repeatedly.


### <Image will go here soon>


## Requirements
- Python 3.7+
- Matplotlib
- Numpy 1.1.7+
- Pandas
- Scipy
- torch

All requirements are in `requirements.txt`, should be easy to install from there I hope.


## Installation
So when I move to a new machine or environment I'll just clone and then add the path of this repo to my ```PYTHONPATH``` environment variable. This way I can freely import it from anywhere without worry. 


## Usage
I prefer to inly import the exact code I need unless doing so will look messy, so the correct (and pythonic) way to import would be to write ```import somecode.distributions as sdist``` or ```import somecode.spectral as sspec``` or whatever you prefer. I don't even think you can import it all in one go if you wanted to.


## Discussion
#### Why???
Very often in day to day work I find myself re-writing the same code again and again, so I thought I'll start making my own scripts where I can just store code and copy/paste when needed. Even this became an issue when I had lots of code saved as a giant string in a txt file, and finding snippets or figuring out what I was thinking back then to write it so badly was a pain. So here is an effort to formally write down the code I use in an easy to use, robust and clean way. Best of all, its tailored to me, so the way the code works and the results I get are just how I like it.

#### Why are there so many small functions???
Well I quite like having lots of small chunks of code to hand, and keeping them all as plain old functions, ready to pull out and use whenever I need them is very convinient. In addition, the code is designed to handle many edge cases, do all type conversions, and generally ensure that things run safely. I just find a stream of multiple discrete functions attached end to end in a line to be the easiest and most intuitive way of doing things. It mimics how I work in data science where a simple and manageable flow of information is preferred. 

#### So you want chunks of code to be ready to use with minimal effort, but what if youre functions become too small? Then you have to call many of them to do simple things and it becomes the same issue you started with!!!
Well yes, but actually no. I clump peices of code from other packages together into functions based on what concept I'm trying to implement or task I'm trying to solve. For example, plotting the distribution and checking how normal the distribution is are two distinct concepts or tasks. They will have their own distinct functions, and will be called seperately one after the other in whatever order. Now you may realise that there is a potential for significant overlap between the two functions, in how you convert the data to Numpy arrays, reshape and create histograms etc. These will split out into their own functions, which are then called from within the larger functions which will be called something like ```plot_distributions()``` or ```assess_distribution()``` etc. But this further discretisation is ONLY a result of having repeated code, and serves only to reduce the problem of haing too much small code occuring again and again (it's usually nicer to do something in 3 lines than 10). And the discretisation stops there. I will NEVER write split functions if that particular code will never be called again in a simliar way. 

#### How will this pacakge develop over time???
I intend to slowly accumulate useful stuff in here as I find myself using it again. So if next week I realise I have to write something to plot the ACF of a timeseries, and I remember that I've had to do that from scratch like 15 times in the past, I'll do it from scratch anyway, but then add it to this repo. 

#### Will there be proper documentation and tests?
Documentation yes. I intend to get some helpful and nice looking documentation written soon which will act both as a guide for me and a live tracker of what I've done. Tests maybe not. It would be cool in theory but I mean this code is really only just for me so I dont think I'll be particularly bothered to do proper testing/CI. 


## Documentation
Documentation is provided <a, href="">here</a>. Its still growing, I hope I'll be able to maintain it well...

## Contributing
Feel free to suggest any issues or improvements, but keep in mind the only reason I'm putting this here is just version control really. Public because maybe someone can use something one day. Please do suggest improvements but remember the code is made in my style, designed for use how I like it.

### License
MIT. Do what you like.
