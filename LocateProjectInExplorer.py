bl_info = {
    "name": "Locate Project In Explorer",
    "description": "Locates the .blend file in Windows Explorer",
    "author": "Nekupaska",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "Search Menu > Locate Project In Explorer",
    "doc_url": "https://github.com/Nekupaska/LocateProjectInExplorer",
    "support": "COMMUNITY",
    "category": "System",
}

import bpy
import subprocess

#############
def openWindowsExplorer(path):
        subprocess.Popen(f'explorer /select,"{path}"')

#############
class LocateProjectInExplorer(bpy.types.Operator):
    bl_idname = "wm.locate_project_in_explorer"
    bl_label = "Locate Project In Explorer"

    def execute(self, context):
        path = bpy.data.filepath.replace('\\\\','\\')
        openWindowsExplorer(r""+path)
        return {'FINISHED'}

#############
# Register (required to also use F3 search "Open Project Location In Explorer" for quick access).
def register():
    bpy.utils.register_class(LocateProjectInExplorer)

def unregister():
    bpy.utils.unregister_class(LocateProjectInExplorer)

if __name__ == "__main__":
    register()
