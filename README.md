morgankeys.com
================

My personal portfolio site built on flask.

You can see it running live here: http://morgankeys.com/

# Dependencies
- Python 2.7.x
  - Virtualenv
  - Flask
- NPM
  - Boostrap
  - jQuery

# Run
- Uses virtualenv for development
- `npm install` tries to set everything up. It simply runs `virtualenv venv && . venv/bin/activate && pip install flask && cd static && npm install`
- (`. venv/bin/activate` starts the local environment.)
- Once in the proper environment, simply run `npm start` (`python morgankeysdotcom.py`)
- Use `$ deactivate` to deactivate virtualenv.

# GOTCHAS
- Uses Python 2.7 and pip
- Doesn't automatically compile SCSS
- You may need to run `pip install` separately.
(Note: 4/17/15 - The `npm install` script is currently broken while I think about how I want to manage dependencies...)
