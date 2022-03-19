# Computer Memory

## What is it?
### Computer memory is necessary to understand in order to have a deeper comprehension of data structures. Computer memory is where data is stored in an Operating System. There's long-term memory storage (hard drives) and short-term memory storage (RAM). We'll be focusing more on the latter. RAM is where data is processed and manipulated, whereas hard drives store that manipulated data for long periods of time.

## Why is it important?
### We use RAM every time we boot up our computers. Reading this file right now is using up space in your RAM. And we especially use it when making calculations in programming data structures. There are two ways data can be stored in memory: Contiguously and Non-contiguously. Each data structure stores their data in one of these two ways. This is important to understand as both methods have their strengths and weaknesses.

![Understanding memory allocation](https://github.com/joehawkens/data-structures-final/blob/main/Assets/MemoryAllocation.PNG)


## Let's look at said strengths and weaknesses of each memory allocation technique:

|Contiguous|Non-contiguous|
|-----------|--------------|
|Faster in execution |Slower in exectuion|
|Easier for OS to control|Harder for OS to control|
|Wastes memory|Saves memory|
|Overhead (time-wasting operations) are minimum|Overhead is more common|
|Internal and External fragmentation can occur | Only External fragmentation can occur|

## But what is Internal and Exteral fragmentation?
### Fragementation what happens in the process of memory allocation. When memory is used up by a process and then finishes that process, it opens up that space for the next process, however, with multiple processes of varying sizes coming and going at once, many free spaces are broken down into unusable, wasted memory.



# Algorithms and Data Structures


## What are they?

### Data Structures, as the name implies, are ways to structure data. Each data structure organizes data differently and because of this, some data structures are better suited than others for solving problems. In addition to this, Algorithms are used with data structures to sort through the data to manipulate it in some way (add, remove, replace, retrieve, etc).

![Data Structures and Algorithms with legos.](https://github.com/joehawkens/data-structures-final/blob/main/Assets/AlgorithmsDiagram.PNG)

### Data Structures and Algorithms are dependent on each other. You can't sort through data with algorithms if it isn't structured in some way and there's no point in structuring data if you don't plan to do anything with it.
  
# When to use it? (Big-O Notation)

## Data Strucutres and Algorithms are the tools of the trade in Software Engineering, much like how a construction worker uses tools at a construction site. Some tools are better suited for certain problems based on the context of the problem(i.e. you wouldn't use a hammer to paint a wall). Therefore, it's important to understand your problem before picking your tools. But how will you know when to use one data structure or algorithm over the other? The answer lies in Big-O Notation: The O in Big-O notation stands for Order of Magnitude, so it's called Big Order of Magnitude because it aims to give you an idea of how much longer it will take to solve a problem as the inputs of data gets bigger and bigger. The scale used to measure the speed of algorithms is called "Time complexity" and is measured thus:



|Fastest||||||Slowest|
|---|---|---|---|---|---|---|
|O(1) | O(log n) | O(n) | O(n log n) | O(n^2) |O(2^n) | O(n!)|


![Big-O Notation Time Complexity for Operations](https://pbs.twimg.com/media/CRW23IcWEAAgpdd.png)

## As made clear by the diagram, each Data Structure carries unique strengths and weaknesses when managing large input. When measuring time complexity it's best to use the "Worst Case Scenario" as a guide for selecting a Data Structure that fits your needs, Worst Case Scenario gives you the performance of a Data Structure at it's very worst, meaning the worst it could possibly get depending on the input given it. If it has a fast speed in Worst Case Scenario, it's usually a safe bet. However, this shouldn't be the only thing that determines your choice of data structure.


## Examples of when to use certain data strucutres....
