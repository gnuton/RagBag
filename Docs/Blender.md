![BlenderLogo](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Logo_Blender.svg/300px-Logo_Blender.svg.png)

# MESH #
## Modeling ##

### Hiding objects ###
If you work in a scene, hiding objects close to the one you are working on is quite convinient.
1. Go To object mode
2. Select the object you want do not want to hide
2. Press Shift-H
To show all other objects again press ALT-H
Note: if you are in edit mode those shortcuts works too but for part of the same object.

### Movement ###

#### Move cursor to center ####
SHIFT-C Moves the curso to center and zooms in

#### Move selection to origin####
1. Move cursor to origin by pressing SHIFT C
2. SHIFT-S > Selection to Cursor

#### Change origin ####
CTRL-ALT-SHIFT-C 

### Curves ###
#### Paths ####
How to make tubes with paths
0. SHIFT-A > Curves > Path
1. Duplicate the above path
2. SHIFT-A > Curves > Nurbs Circle
3. Select the first path
4. From the right panel (property window) select the TAB "curves"
5. Use the picker to select the circle as bevel object (if this is right your path will become a tube)
6. Use the picker to select the other path as Taper object (the tube will disappear!)
7. Select the path used as Taper object.
8. Press TAB to enter edit mode
9. Select one or more vertices and translate it/them on the Y (green) axis to modify the taper of the tube
10. You can now edit the shape of the tube from moving the vertices of the the main path in edit mode
11. Add a "decimate" modifier at the mesh and use Un-Subdivide and Increase Iteration as long as the mesh looks okay.
11. Once you have done, if you wanna get a mesh out of the tube, select the tube,  press ALT-C and press Mesh from Curve
## Sculpturing ##
## Poly reduction ##
### Retopoflow ###

# TEXTURE #
## UV Unwrapping ##
### Basic Unwrapping ###
Smart UV Project is fastest way to automatically unwrap your mesh:
- GOOD if you use texture paiting.
- NOT VERY GOOD if you wanna place a simple texture, because there will be some cuts visible on it.

To Unwrap a mesh automatically:
0. Select the object to unwrap
1. Enter Edit Mode
2. Press U
3. Select "Smart UV Project"
4. Open "UV Image Editor" view. The unwrap will be shown there.

### Basic Manual Unwrapping ###
Mnual unwrapping works so that you define the cuts (seems).
The seems define cuts in the mesh.
Rule of thumb:
- A cut usually goes where there are 90 degrees angles.
- Some cut are fine to be seen, other don't.

Process:
0. Select the object
1. Select the edges to become seems
2. Press CTRL-E > Mark Seem
3  Repeat 2 and 3 until  you have define the cuts you want.
4. In the UV Image Editor" press N to show the tool bar on the right side and select "Stretch" from UV>Outline tab.
5. Repeat 2-3 until the unwrapped texture doesn't become comletely blue. If it's light blue it means it' stretched and 
   there the texture will look bad.
6  If  you want to remove all seems, press A (to select all edges) > CTRL E > Clear Select

### Optimize the Texture ###
Once unwrapped, in the UV/Image Editor we can scale (S), Rotate(R) and Move (G) the Isles (pieces of textures) once selected with L.

### Unwrap multiple objects ###
#### Method A - unwrap objects all together ####
1. Select the objects to unwrap
2. Press enter and write "smart UV Project"
https://www.youtube.com/watch?v=Cuj0Oypj_ic

#### Method B - unwrap object one at time ####
1. Select the object and unwrap with a method describe above.
2. Do the same for the same object
3. In object mode select the objects you want to see the UV
3. In the Image/UV Editor view click "Draw other objects" to see the UV of the selected objects side by side

#### Use a single mapping for several objects ####
This will work if the meshes of the objects to unwrap have the same geometry
1. Select the objects to unwrap
2. Select at last the object with UV mapping
3. Press CTRL-L > Transfer UV Map

## Texture Hand Paiting ##
0. Select the object to texture paint
1. Unwrap by following the automatic procedure described in the previous chapter
2. In the image UV Editor click NEW in the toolbar at bottom
3. Select the resolution of the texture, black and create it.
4. Select Cycle as Render engine
5. Add a material to the mesh by clicking The red sphere icon in the toolbar on the right side of the viee and then press new
6.  In the node editor view press SHIFT A to and add Texture> Image Texture > Select the image created in the UV Editor
7.  Switch to Texture paint in the 3d View
8. Remember to save the texture or you will use it.

## Normal Map ##
### Baking normal map from hi-res content on top of a Multires modifier ###
1. select all object
2. press SPACE BAR
3. write "smart unwrap"
4. In the message box press OK

Now to see if it worked select 1 object, go to edit mode by pressing TAB and you will see highlighted in the image the UV mapped texture.
https://www.youtube.com/watch?v=_0FwsMkWm0k

0. Select only one mesh for baking normal map. The mesh has to be made of squares and not triangles. You can achieve that using for instance a cube and applying a subdiv modifier on it
1. If a sphere press SPACE and click to Sphere
2. In object more, from the panel on the left side under "tools" page click smooth. If you do not do that you will see the mesh subdivision into the normal map.
1. Be sure it's unwrapped and the image associated is selected in the node editor. If not create a material and add Image texture boxe in it, then set the image and keep it highlighted.
2. Use multires modifier on that object
3. Raise the levels of subdivisions as high as I need to have nice details
4. Created details in sculpt mode, go to Cycles Render Engine
5. Go to "Render" tab and open "Bake" option
6. "Selected to Active" is disabled (becaused baking normal maps with this option is based on other method)
7. Change "Bake Type" to "Normal"
8. Hit the "Bake" button and be happy to have good normal map.

This way of baking normal maps for mesh is usually used when your mesh has fine topology (the mesh consists of square-shaped faces and not triangles), because multires modifier will subdivide all faces and mesh that consists of triangles, will deform the mesh alot. However, it's easier to subdivide squares and it doesn't cause any problems this way.
## MATERIALS ##
### Shaders ###
#### Shader for testing normal maps ####
Image Texutre -> Normal Map -> Glossy BSDF ->  (Fac)   Mix Shader -> Material Output
                            -> Diffuse BSDF -> (shader)
                               Fresnel      -> (shader)
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)

## MODIFIERS ##
### Array ###
#### Place element circularly around an object ####

## Troubleshoots ##
### Camera doesn't zoom anymore ###
In Blender you can rotate around an point and zoom in and out, for some reasons from time to time zooming in is not possible anymore. You can press '.' in the numerica pad to workaround this issue.


## Extra reading ##
### Diffuse map
### Normal map
* [Shader fundamentals - Normal Mapping](https://www.youtube.com/watch?v=6_-NNKc4lrk)
* [Normal Maps vs Bump Maps vs Height Maps](https://cgcookie.com/articles/normal-vs-displacement-mapping-why-games-use-normals)
