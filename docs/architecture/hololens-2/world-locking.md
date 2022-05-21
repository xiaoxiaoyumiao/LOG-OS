# World Locking

## Installation

## Mechanism

- https://microsoft.github.io/MixedReality-WorldLockingTools-Unity/DocGen/Documentation/Concepts/Advanced/SessionOrigin.html

## Persistence

- Main doc: https://docs.microsoft.com/en-us/mixed-reality/world-locking-tools/documentation/howtos/usingwlt/persistencetricks
- Introduction - with ASA: https://docs.microsoft.com/en-us/windows/mixed-reality/develop/unity/shared-experiences-in-unity
- Anchor subsystem: WSA seems deprecated in U2020 
    - https://github.com/microsoft/MixedReality-WorldLockingTools-Unity/issues/162

## WLT+ASA

- main doc: https://docs.microsoft.com/en-us/mixed-reality/world-locking-tools/documentation/howtos/wlt_asa
- A startup sample: https://docs.microsoft.com/en-us/mixed-reality/world-locking-tools/documentation/howtos/samples/wlt_asa_sample
    - Remember to add the `wifiControl` line.
- (Prerequisite: install WLT) Register Azure account (can use education ver) and obtain the acount ID, domain & key (for certification in package): https://docs.microsoft.com/en-us/azure/spatial-anchors/quickstarts/get-started-unity-hololens?tabs=azure-portal
- startup configuration: https://docs.microsoft.com/en-us/azure/spatial-anchors/how-tos/setup-unity-project?tabs=xr-plugin-framework%2Cunity-2020%2Cunity-package-mixed-reality-feature-tool%2CExtraConfigurationsHoloLens
    - be sure to enable SpatialPerception, InternetClient and PrivateNetworkClientServer in Project Settings -> Player -> (under Universal Windows Platform tab) -> Publishing Settings -> Capabilities. Ref: https://docs.unity3d.com/Manual/class-PlayerSettingsWSA.html

## References

- Installation (by unity package releases): https://docs.microsoft.com/en-us/mixed-reality/world-locking-tools/documentation/howtos/wltviamrfeaturetool#wlt-releases-unitypackage-files
- Releases: https://github.com/microsoft/MixedReality-WorldLockingTools-Unity/releases
- https://docs.microsoft.com/en-us/windows/mixed-reality/develop/unity/spatial-anchors-in-unity?tabs=wlt
- https://docs.microsoft.com/en-us/mixed-reality/world-locking-tools/documentation/howtos/initialsetup
- Sample: https://docs.microsoft.com/en-us/mixed-reality/world-locking-tools/documentation/howtos/samples/spacepin
- Sample: https://microsoft.github.io/MixedReality-WorldLockingTools-Samples/Tutorial/01_Minimal/01_Minimal.html
- Visualizer: https://docs.microsoft.com/en-us/mixed-reality/world-locking-tools/documentation/howtos/tools
- https://docs.microsoft.com/en-us/mixed-reality/world-locking-tools/documentation/concepts/advanced/spacepins
- https://docs.microsoft.com/en-us/mixed-reality/world-locking-tools/documentation/howtos/usingwlt/alignmycoordinates
- Far interaction: https://docs.microsoft.com/en-us/windows/mixed-reality/design/gaze-and-commit