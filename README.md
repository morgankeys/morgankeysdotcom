morgankeys.com
================

My personal portfolio site built on flask.

You can see it running live here: http://morgankeys.com/

#Run
- Uses virtualenv for development
- You can use `npm install` to set everything up. It simply runs `virtualenv venv && . venv/bin/activate && pip install flask && cd static && npm install`
- (`. venv/bin/activate` starts the local environment.)
- Once in the proper environment, simply run `npm start` (`python morgankeysdotcom.py`)

#GOTCHAS
- Uses Python 2.7 and pip
- Doesn't automatically compile SCSS
