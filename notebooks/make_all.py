f = open("test.ipynb","w")
q = r""" 
,{
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "BlarBlarBlar"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": "print \"Hello, IPython\"",
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": "Hello, IPython\n"
      }
"""

x = r"""{
 "metadata": {
  "name": "simple"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": "The simplest notebook."
    }
    """+q+"""
     ],
     "prompt_number": 1
    },
         ],
     "prompt_number": 1
    }
   ],
   "metadata": {}
  }
 ]
}
"""

f.write(x)
f.close()
