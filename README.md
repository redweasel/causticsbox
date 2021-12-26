# CausticsBox
This is a side project along studying physics at university.

### Goals
 - A simple python "game-like" program to simulate caustics in 2D in realtime for educational purposes
 - should include optic elements like simple lenses, mirrors and absorbers
 - minimal gui to place optic elements and shine lights through the system
Potential things to include if we get bored of the simple optic elements:
 - color filters, dichromic mirrors
 - dispersive and diffuse optic elements
 - interference of coherent light sources
 - polarisation property of light rays (limited as it would still be 2D)

### Workplan
This should be possible using PyGame as graphics and input library.
After programming a basic window which can render lines and text, these are the things to do:
- [x] Using the mouse position as light source and the borders of the window as mirrors, implement the basic algorithm to shine light into the empty scene. This will be done by rendering many lines on top of each other in additive blend mode. (few hours worktime)
- [ ] Implement line-line intersection testing and make a simple tool to make straight mirrors/absorbers by clicking and dragging. (few hours worktime)
- [ ] make elements snap to a grid while placing and implement selection of elements to tweak them or change their properties. (~1 hour worktime)
- [ ] add a simple slider UI element to tweak the absorbtion of a mirror from 0 to 1. (~1 hour worktime)
- [ ] add lines with snells law instead of reflection. Use many of them in combination to make simple spherical lenses which are placeable on the grid. (~2 hours worktime)
- [ ] make a good UI to design the spherical lenses and visualize their sphere centers and focal points. (few hours worktime)
- [ ] add a UI to show available keyboard shortcuts in the lower right corner using the TAB key. (10 min worktime)
- [ ] add additional placeable light sources with tweakable brightness. (30 min worktime)
- [ ] implement a more efficient algorithm for line-line intersection when there are lots of (connected) lines. Either a BVH with AABBs since the structure of the lines is mostly known or a simpler sweep and prune algorithm for O(n log n) time complexity. (few hours worktime)
- [ ] Design a fancy icon for the app. (creative tasks are hard to put time estimates on...)
- [ ] 
The steps above don't need this particular order so work can be done on multiple things in parallel. Also time estimates may be too low if someone needs to do some serious learning to do one of the tasks.
