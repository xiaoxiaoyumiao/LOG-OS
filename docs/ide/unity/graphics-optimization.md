# Graphics Optimization

## Mesh Optimization

### Model simplification in Unity

Here is a useful tool: https://github.com/Whinarn/UnityMeshSimplifier

Introduction: https://www.youtube.com/watch?v=5y4quM0a_js

Installation: https://github.com/Whinarn/UnityMeshSimplifier/wiki/Installing-through-package-manager

Sample Code (Add a button in inspector of `SimplifyMesh`; will store the simplified mesh to Assets/Prefabs/[mesh_name].asset):

```c#
      /* SimplifyMesh.cs */
      using UnityEngine;
      
      public class SimplifyMesh : MonoBehaviour
      {
          public float quality = 0.5f;
      }
      
      /* SimplifyMeshEditor.cs */
      using UnityEngine;
      using UnityEditor;
      
      [CustomEditor(typeof(SimplifyMesh))]
      public class SimplifyMeshEditor : Editor
      {
          public static string SaveMesh(Mesh mesh, string name, bool makeNewInstance, bool optimizeMesh)
          {
              string path = "Assets/Prefabs/"+ name+ ".asset";
              Debug.Log(path);
              Mesh meshToSave = (makeNewInstance) ? Object.Instantiate(mesh) as Mesh : mesh;
      
              if (optimizeMesh)
                  MeshUtility.Optimize(meshToSave);
      
              AssetDatabase.CreateAsset(meshToSave, path);
              AssetDatabase.SaveAssets();
              return path;
          }
      
          public override void OnInspectorGUI()
          {
              base.OnInspectorGUI();
              var simplifyMesh = target as SimplifyMesh;
              if (GUILayout.Button("Simplify Mesh"))
              {
                  var filters = simplifyMesh.GetComponentsInChildren<MeshFilter>();
                  for (int i=0;i<filters.Length;++i)
                  {
                      var filter = filters[i];
                      Debug.Log(filter);
                      var originalMesh = filter.sharedMesh;
                      var meshSimplifier = new UnityMeshSimplifier.MeshSimplifier();
                      meshSimplifier.Initialize(originalMesh);
                      meshSimplifier.SimplifyMesh(simplifyMesh.quality);
                      var destMesh = meshSimplifier.ToMesh();
                      string path = SaveMesh(destMesh, originalMesh.name + "_" + i.ToString(), true, true);
                      var newMesh = (Mesh)AssetDatabase.LoadAssetAtPath(path, typeof(Mesh));
                      filter.sharedMesh = newMesh;
                  }
              }
          }
      }
```

ref: 
    - https://answers.unity.com/questions/39311/editor-scripting-how-to-save-a-script-generated-me.html
    - https://github.com/pharan/Unity-MeshSaver/blob/master/MeshSaver/Editor/MeshSaverEditor.cs 
    - https://forum.unity.com/threads/what-does-optimize-mesh-do.346220/

### TMPro SRP shader

preview: https://www.youtube.com/watch?v=oXdEjrm2ry4

source file: https://forum.unity.com/threads/plans-for-hdrp-compatibility-for-tmp.660598/page-2#post-7081120
  
### LOD Group

LOD(Level of Detail) technique specifies mesh with different levels of complexity (how detailed a mesh is) for a 3D object, from which a proper mesh would be chosen when the distance between main camera and 3D object falls in a certain range. By using a simpler mesh when the object is far away, the rendering workload could be reduced.

An LOD level corresponds to a range of distance (strictly speaking, it is determined by the ratio of object's screen space height to screen height). When the position of the object relative to the main camera falls in the range, the mesh of corresponding LOD level is enabled.

With the LOD Group component, you can specify the range boundary of every LOD level and corresponding mesh to use.

Create LOD manually: create a game object (maybe as a prefab) and add LOD Group component to it. Then add meshes of all LOD levels as children of the game object, and as a good practice, suffixing their names with corresponding LOD level (for example, Tree_LOD0, Tree_LOD1). Now you can adjust the range directly, and drag-and-drop these meshes of different LOD levels to the LOD Group component.
  - ref: https://docs.unity3d.com/Manual/class-LODGroup.html

Find all objects in scene with certain shader:

```c#
    using UnityEngine;
     using UnityEditor;
     using System.Collections.Generic;
     
     public class FindShaderUse : EditorWindow {
         string st = "";
         string stArea = "Empty List";
    
         public void OnGUI() {
             GUILayout.Label("Enter shader to find:");
             st = GUILayout.TextField (st);
             if (GUILayout.Button("Find Materials")) {
                 stArea = "";
                 FindShader(st);
             }
             GUILayout.Label(stArea);
         }
         
         private void FindShader(string shaderName) {
             int count = 0;
             stArea = "Materials using shader " + shaderName+":\n\n";
             
             List<Material> armat = new List<Material>();
             
                Renderer[] arrend = (Renderer[])Resources.FindObjectsOfTypeAll(typeof(Renderer));
             foreach (Renderer rend in arrend) {
                 foreach (Material mat in rend.sharedMaterials) {
                     if (!armat.Contains (mat)) {
                         armat.Add (mat);
                     }
                 }
             }
             
             foreach (Material mat in armat) {
                 if (mat != null && mat.shader != null && mat.shader.name != null && mat.shader.name == shaderName) {
                     stArea += ">"+mat.name + "\n";
                     count++;
                 }
             }
             
             stArea += "\n"+count + " materials using shader " + shaderName + " found.";
         }
     }
```

ref: https://answers.unity.com/questions/510945/find-materials-that-use-a-certain-shader.html

### Transparent objects

Sometimes we use textures with part of it set to transparent (alpha=0), and we want these parts to be completely invisible. To do this we need to enable Alpha Clipping in the material setting or otherwise it would be rendered into a glass-like effect.

Transparent objects are expensive to render. Try reduce the number of transparent objects by occlusion culling, LOD grouping or simply removing them.

## Occlusion Culling

By default Unity does frustum culling (cull objects that are outside the view of camera). Occlusion culling further reduces objects that, though fall in the view of camera, may still be occluded by other (large) objects like walls.

Panel: Window -> Rendering -> Occlusion Culling

Select a camera object, adjust parameters in panel, and click "bake" to calculate occlusion culling. Finer parameters lead to larger size of data but would not always give better performance, so just fine-tune it through trial-and-error.

After baking the occlusion culling data, you can see how it's working by the "Visualization" tab in panel. Move around and rotate the camera object to see how objects get culled.

ref: https://docs.unity3d.com/Manual/occlusion-culling-getting-started.html

## Draw Call Batching

### SRP Batcher

https://docs.unity3d.com/Manual/SRPBatcher.html

### Tools

Use Window -> Analysis -> Frame Debugger to see all draw calls.

By changing the inspector mode to Debug (set it at top-right corner of the inspector) you can see much internal information, for example keywords of a material.
    - ref: https://forum.unity.com/threads/srp-batch-problem-node-use-different-shader-keywords.728522/

### Multi-Camera in HDRP

It's bad practice to put multiple cameras in a HDRP scene (will cause the rendering time to multiply). Try to always keep the camera amount to 1.


## Light and Shadow (HDRP)

official guide:
    - https://docs.unity3d.com/560/Documentation/Manual/LightPerformance.html

### Tools

Tune and bake most of the lighting (and shadowing) information in Window -> Rendering -> Lighting.

Use Window -> Render Pipeline -> Render Pipeline Debug to open the debug panel. You can obtain a bunch of useful rendering information here.
    - ref: https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@10.9/manual/Render-Pipeline-Debug-Window.html

Discussion on HDRP: https://forum.unity.com/threads/improving-performance-in-hdrp-7-3-1.878374/

Light layers in HDRP: https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@7.1/manual/Light-Layers.html

### Shadow map:

shadow map rendering can be very costly. If a light component is set to Realtime or Mixed mode, there is an option in the shadow section for enabling shadow map or not. When enabled, there would be a pass for shadow map rendering which can be seen from the frame debugger. Disable the shadow map if it's expensive and unnecessary. If we cannot go without the real time shadows, consider reducing the resolution of the shadow map, or choose a smaller fade distance (or max distance for directional lights).
    - ref: https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@10.2/manual/Shadows-in-HDRP.html

### Lightmaps

It stores lighting information for every static objects. 

### Light Probes

It stores lighting information at a point in an empty space. It's for efficient lighting of a moving object.
  - ref: https://docs.unity3d.com/Manual/LightProbes.html

### Reflection probes

https://docs.unity3d.com/Manual/class-ReflectionProbe.html

I don't know why, but the Use Occlusion Culling option in Reflection Probe component would affect the result of baking. It looks a bit more natural (or maybe just different) when having this option turned on.

## HDRP Post-Processing

### Enable & Disable

All post-processing effects can be managed in Project settings -> HDRP default settings.

### Bloom

Bloom effect creates fringes of a bright light (a fog-like, glowing & blurring effect). This is done for materials with emission effect set.

###  Motion blur

Make a blur for the surrounding environment when it's moving fast.

## References

https://docs.unity3d.com/Manual/OptimizingGraphicsPerformance.html

https://docs.unity3d.com/Manual/SL-ShaderPerformance.html

https://learn.unity.com/tutorial/fixing-performance-problems-2019-3-1#

https://docs.unity3d.com/Manual/ProfilerWindow.html

https://docs.unity3d.com/Manual/FrameDebugger.html

https://learn.unity.com/tutorial/diagnosing-performance-problems#5c7f8528edbc2a002053b598

Mesh:

https://docs.unity3d.com/Manual/class-TextureImporter.html

https://docs.unity3d.com/Manual/ModelingOptimizedCharacters.html

https://docs.unity3d.com/Manual/LevelOfDetail.html

https://docs.unity3d.com/ScriptReference/Rendering.OnDemandRendering.html

https://forum.unity.com/threads/mesh-simplify-quickly-reduce-polygon-count-on-your-3d-models.347057/

http://obi.virtualmethodstudio.com/forum/archive/index.php?thread-2227.html

https://forum.unity.com/threads/what-would-be-an-ideal-poly-count-for-a-mobile-racing-game.487455/

https://docs.unity3d.com/Packages/com.unity.formats.fbx@2.0/manual/index.html

https://forum.unity.com/threads/export-unity-mesh-to-obj-or-fbx-format.222690/

https://www.reddit.com/r/3dsmax/comments/1f8a9b/help_how_to_reduce_polygon_count_after_model/

3ds max:

https://docs.microsoft.com/en-us/dynamics365/mixed-reality/guides/3d-content-guidelines/3ds-max#optimize-a-3d-model

optimizers: https://knowledge.autodesk.com/support/3ds-max/learn-explore/caas/CloudHelp/cloudhelp/2022/ENU/3DSMax-Modeling/files/GUID-99A80959-7100-440E-BC06-17E79E13F8A5-htm.html

multires: https://knowledge.autodesk.com/support/3ds-max/learn-explore/caas/CloudHelp/cloudhelp/2019/ENU/3DSMax-Modifiers/files/GUID-DFD94E0F-7B08-4945-A176-42B49B8F458E-htm.html

multires manual: https://help.autodesk.com/view/3DSMAX/2017/ENU/?guid=__files_GUID_D41213A1_D125_4349_912C_071A32E94113_htm

https://help.augment.com/en/articles/2646887-autodesk-3ds-max-reducing-the-polygons-count

https://forums.autodesk.com/t5/3ds-max-forum/preserve-uvw-maps-after-optimise-or-another-way-to-decrease/td-p/4219574

pro optimizer: https://knowledge.autodesk.com/support/3ds-max/learn-explore/caas/CloudHelp/cloudhelp/2020/ENU/3DSMax-Modifiers/files/GUID-86DDCD03-C817-4DB6-8041-207D17C8CB59-htm.html

HDRP:

https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@7.1/manual/Upgrading-To-HDRP.html

https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@13.1/manual/System-Requirements.html

Graphics API setting:

https://docs.unity3d.com/Manual/GraphicsAPIs.html