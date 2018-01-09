__________.__                     .___            
\______   \  |   ____   ____    __| _/___________ 
 |    |  _/  | _/ __ \ /    \  / __ |/ __ \_  __ \
 |    |   \  |_\  ___/|   |  \/ /_/ \  ___/|  | \/
 |______  /____/\___  >___|  /\____ |\___  >__|   
        \/          \/     \/      \/    \/       
        
= TEXTURE =
== UV Unwrapping ==
=== Basic Unwrapping==
Smart UV Project is fastest way to automatically unwrap your mesh:
- GOOD if you use texture paiting.
- NOT VERY GOOD if you wanna place a simple texture, because there will be some cuts visible on it.

To Unwrap a mesh automatically:
0. Select the object to unwrap
1. Enter Edit Mode
2. Press U
3. Select "Smart UV Project"
4. Open "UV Image Editor" view. The unwrap will be shown there.

=== Basic Manual Unwrapping ===
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

=== Optimize the Texture ===
Once unwrapped, in the UV/Image Editor we can scale (S), Rotate(R) and Move (G) the Isles (pieces of textures) once selected with L.

==Texture Hand Paiting ===
0. Select the object to texture paint
1. Unwrap by following the automatic procedure described in the previous chapter
2. In the image UV Editor click NEW in the toolbar at bottom
3. Select the resolution of the texture, black and create it.
4. Select Cycle as Render engine
5. Add a material to the mesh by clicking The red sphere icon in the toolbar on the right side of the viee and then press new
6  In the node editor view press SHIFT A to and add Texture> Image Texture > Select the image created in the UV Editor
7  Switch to Texture paint in the 3d View
8 Remember to save the texture or you will use it.


