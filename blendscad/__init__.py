# blendscad - Init the core functionality
# by Michael Mlivoncic, 2013

#import os
import bpy


#default layers for all objects
mylayers = [False]*20
mylayers[0] = True

mat = None

def main():
	global mat, matTrans, defColor, fa, fs, fn
	# need to setup our default material
	mat = bpy.data.materials.get('useObjectColor')
	if mat is None:
		mat=bpy.data.materials.new('useObjectColor')
		mat.use_object_color=1		
	# for Grouping, "invisible", but selectable :-)
	# need to be in "Texture" Display mode...
	matTrans = bpy.data.materials.get('Transparent')
	if matTrans is None:
		matTrans=bpy.data.materials.new('Transparent')
		matTrans.use_transparency=True
		matTrans.transparency_method='Z_TRANSPARENCY'
		matTrans.alpha = 0.0	
	# some colors... 
	#black = (0.00,0.00,0.00,0)
	#yellow = (1.00,1.00,0.00,0)
	# for full color list:
	#sys.path.append("<path to>/BlendSCAD") 
	#from blendscad_colors import *
	# default color for object creators below...
	defColor = (1.0,1.0,0.1,0)
	#Emulate OpenSCAD Special variables  blendscad.{fs,fa,fn}
	#$fa - minimum angle  $fn = 360 / $fa    / default: $fa = 12 -> segments = 30
	fa=12;
	#$fs - minimum size   default: 1 
	fs=1;
	#$fn - number of fragments  | override of $fa/$fs , default = 0 , example: 36-> every 10 degrees
	fn=0;
	if bpy.context.active_object is not None:
		if bpy.context.active_object.mode is not 'OBJECT': 
			bpy.ops.object.mode_set(mode = 'OBJECT')
	
# from blendscad.colors import *
# from blendscad.math import * 
# from blendscad.core import *
# from blendscad.primitives import *
# from blendscad.impexp import * # import, export, surface

# "reload()" is not reliable, especially with "from ... import *"
# better using exec(compile(...)) instead while developing the modules..
# ####################################################################
# # This block helps during developmentas it reloads the blendscad modules which are already present
# # and may have changed...
# # can be commented out or removed if you do not modify blendscad libs during this blender session.
# import imp; import sys
# rel = ['blendscad','blendscad.math',
# 'blendscad.core', 'blendscad.primitives','blendscad.impexp', 'blendscad.shapes']
# for mo in rel:
	# if mo in sys.modules.keys():
		# print ('reloading: '+mo+' -> '+ sys.modules[mo].__file__)
		# imp.reload(sys.modules[mo])
# ####################################################################


# init blendscad in current namespace, so no need to type blendscad.cube()
# similar to exported functions of a module....
def initns(nsdict):
	import sys
	import blendscad
	import blendscad.colors
	import blendscad.math
	import blendscad.core	
	import blendscad.primitives
	import blendscad.impexp
	#import blendscad.shapes
	try:
		import __builtin__
	except ImportError:
		import builtins as __builtin__ #Python 3.0
	
	# all colors -> expecting nothing private in color file..
	for name in dir(blendscad.colors):
		if name.find("__") < 0 and name !="bpy":
			nsdict.update({name: getattr(blendscad.colors, name)  })			
	#
	if blendscad.mat is None:	
		blendscad.main()
	# >>> print( dir(blendscad.primitives))		
	public_prim = [ 'circle', 'cube', 'cylinder', 'mylayers', 'polygon', 'polyhedron', 'sphere', 'square']		
	for name in public_prim:
		nsdict.update({name: getattr(blendscad.primitives, name)  })	
	#
	public_core = [  'listAllObjects', 'clearAllObjects', 'color', 'echo', 'str'
	                 ,  'difference', 'union', 'intersection', 'join', 'group'
					 , 'resize', 'rotate', 'mirror', 'translate', 'scale'
	                 , 'hull', 'linear_extrude', 'rotate_extrude', 'projection'
					 , 'remove_duplicates', 'round_edges', 'cut'
					# call those more explicitly... blendercad.core.* 
					# ,'booleanOp', 'remesh','cleanup_object', 'dissolve', ''
				]
	for name in public_core:		    
		nsdict.update({name: getattr(blendscad.core, name)  })
	#>>> print( dir(blendscad.math))
	public_math = [  'true','false', 'rands','acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'exp', 'floor', 'ln'
					, 'log', 'lookup', 'math', 'pi', 'sign', 'sin', 'sqrt', 'tan']
	for name in public_math:	
		nsdict.update({name: getattr(blendscad.math, name)  })
	#		
	public_impexp = [  'export', 'export_dxf', 'export_stl', 'fill_object', 'import_', 'import_dxf', 'import_stl', 'surface']
	for name in public_impexp:	
		nsdict.update({name: getattr(blendscad.impexp, name)  })					
	#
	#print("Registered all public BlendSCAD functions to namespace")
	
			 
			 
if __name__ == "__main__":
	main()
	
	




