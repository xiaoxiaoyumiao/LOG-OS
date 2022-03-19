# Interface Mapping in Unity Wrapper

| HairWorks API | HairWorksIntegration API | Function |
| :--- | :--- | :--- |
| `loadSdk` | `hwLoadHairWorks` | Load the library |
| `loadAsset` | `hwAssetLoadFromFile` | Load the hair asset |
| `loadAsset` | `hwAssetReload` | Load the hair asset |
| `initRenderResources` | `hwInitialize` | Init D3D runtime globally |
| `setCurrentContext` | `hwInitialize` | Init D3D context |
| `createInstance` | `hwInstanceCreate` | Create a hair instance |
| `freeInstance` | `hwInstanceRelease` | Release a hair instance |
| `setViewProjection` | `hwSetViewProjection` | Set view & projection mat |
| `updateInstanceDescriptor` | `hwInstanceSetDescriptor` | Change instance param |
| `getInstanceDescriptor` | `hwInstanceGetDescriptor` | Read instance param |
| `stepSimulation` | `hwStepSimulation` | Sim motion for 1 frame |
| `updateSkinningMatrices` | `hwInstanceUpdateSkinningMatrices` | Skinning linear upd |
| `updateSkinningDqs` | `hwInstanceUpdateSkinningDQs` | Skinning dualquat upd |
| `PSSetShader` | `hwSetShader` | Set hair pixel shader |
| `preRender` | `hwRender` |  |
| `renderHairs` | `hwRender` | Render hairs |
| `renderHairs` | `hwRenderShadow` |  |
| `freeInstance` | `hwInstanceRelease` | Release hair instance |
| `freeAsset` | `hwAssetRelease` | Release hair asset |
| `release` | `hwUnloadHairWorks` | Unload the library |

