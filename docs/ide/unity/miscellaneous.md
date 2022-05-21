# Miscellaneous

* 一个带有member的class被绑定到一个游戏中的实体（拖动放置到实体）时，实体会多出一个与class名字一致的属性组（在unity里似乎叫做component），且具有与member一致的子属性。如果script更新，unity中的属性也会随之更新。
* 碰撞盒是一类常用的component，包括box collider 2d和rigidbody 2d等
* 若需要为 Unity 项目添加 reference，在 VS 的项目浏览面板中选择 csharp project 中的 references，展开，点击 Analyzers，在 Project 菜单中选择 Add Reference.(ref: \[2])
* 如何在 VS 中查看项目的 properties：

> You have to enable the "Access to project properties" option in the Tools>Options>Tools for Unity>General" section.   (ref: \[3])

* 使用 transform.parent 获取父对象。
* 如果想在查看场景时让场景视角绕一个物体旋转，可选定该物体后按 Alt + 鼠标左键拖动即可。(ref: \[5])

- In the hierarchy window, type `t:ComponentName` to filter objects with component `ComponentName`. For example, `t:light` filters all lighting objects.

    - ref: https://forum.unity.com/threads/show-all-colliders-in-editor-solved.60352/

- Quick Search

    - A tool to help search in scenes/assets for objects by a wide range of properties
    - ref: https://docs.unity3d.com/Packages/com.unity.quicksearch@2.1/manual/search-syntax.html

- View & edit colliders in scene: use Windows -> Analysis -> Physics Debugger

    - ref: https://forum.unity.com/threads/is-there-a-way-to-show-all-physics-colliders-without-having-to-select-a-collider.1081940/

- Change viewing perspective of editor scene

    - Click on the coordinate axes at top-right corner of the scene. Clicking on the center cube switches between perspective / orthographic
    - ref: https://answers.unity.com/questions/1246988/editor-scene-how-to-change-2d-view-direction.html

- Icons of gameObjects
    - You can assign icons to gameObjects in the top-left corner of the inspector.
    - After assigned, the icon would appear on top of the gameObject in the scene. This is suitable for displaying empty objects (points, etc.)
    - ref: https://docs.unity3d.com/2019.3/Documentation/Manual/AssigningIcons.html

- Turn off some icons of objects
    - Some objects have icons marked in scene by default(texts, lights, etc.) These icons can be managed in **Gizmos** in the button group on top of the scene.

- Sample code: generate a grid map according to colliders in scene

```c#
    	// Only consider colliders in this layer
    	public LayerMask boundaryLayer;
    	// Texture that displays gridmap information by pixels
    	public Texture2D gridInfo;
    	// UI Image that renders the gridInfo texture (in World Space canvas)
    	// We'll make it aligned with the physical colliders for visualization
    	// The map is centered at (0, 0, 0)
    	// Canvas position: 0, 0, 0 rotation: 90, 0, 0
    	public Image gridDisplay;
    
    	// Size (width & height) of a grid, in Unity unit
    	// By width & height we refer to the range along x & z axis
    	//     (Since it's width & height of the 2d map)
    	public float gridSize;
    	// A y-axis range to filter out colliders 
    	//     that won't collide with the main character.
    	public float robotYMax;
    	public float robotYMin;
    	
    	// Stores grid map information. simulate 2darray with 1darray
    	int[] gridOccupied;
    	// Stores width(W) and height(H) of the map
    	int gridArrWidth, gridArrHeight;
    	// logical coordinate of grids ranges from (-W/2, -H/2) to (W/2, H/2).
    	// With offsets We maps the range to non-negative 1darray indices
    	int xOffset, zOffset;
    	public void GenerateGrid()
    	{
            // Extent(half of width/height) of the bounding box in Unity unit
            // Here it's 30m * 30m
    		float boundaryX = 30;
    		float boundaryZ = 30;
    
            // Calculate W & H (logical range of grids)
    		int width = 2 * (int)(boundaryX / gridSize) + 1;
    		int height = 2 * (int)(boundaryZ / gridSize) + 1;
    		gridArrWidth = width;
    		gridArrHeight = height;
    		gridOccupied = new int[width * height];
    
            // Change size of the image accordingly to align it with the colliders
    		gridDisplay.rectTransform.SetSizeWithCurrentAnchors (RectTransform.Axis.Horizontal, width * gridSize);
    		gridDisplay.rectTransform.SetSizeWithCurrentAnchors (RectTransform.Axis.Vertical, height * gridSize);
    
            // Initialize the texture to pure white and change the filter mode
            // This disables anti-aliasing when stretching the bitmap texture
    		gridInfo = new Texture2D(width, height);
    		gridInfo.filterMode = FilterMode.Point;
    		var fillColorArray = new Color[gridInfo.width * gridInfo.height];
    		for (var i = 0; i < fillColorArray.Length; ++i)
    		{
    			fillColorArray[i] = Color.white;
    		}
    		gridInfo.SetPixels(fillColorArray);
    		gridInfo.Apply();
    
    		xOffset = width / 2;
    		zOffset = height / 2;
            // Iterate over all colliders in the scene
            //     (expensive but we do it only once)
    		var colliders = FindObjectsOfType<Collider>();
    		foreach (var collider in colliders)
    		{
                // We don't care about triggers
    			if (collider.isTrigger) continue;
                // Filter by layer
    			if ((boundaryLayer.value & (1 << collider.gameObject.layer)) != 0)
    			{
                    // Get bounding box and calculate a smallest grid rectangle
                    //    that covers the bounding box
    				var bound = collider.bounds;
    				if ((bound.max.y < robotYMin) || (bound.min.y > robotYMax)) continue;
    				int xMax = Mathf.Min(width - 1, Mathf.CeilToInt(bound.max.x / gridSize - 0.5f) + xOffset);
    				int xMin = Mathf.Max(0, Mathf.FloorToInt(bound.min.x / gridSize + 0.5f) + xOffset);
    				int zMax = Mathf.Min(height - 1, Mathf.CeilToInt(bound.max.z / gridSize - 0.5f) + zOffset);
    				int zMin = Mathf.Max(0, Mathf.FloorToInt(bound.min.z / gridSize + 0.5f) + zOffset);
    				
                    // Fill in the array and the texture
    				for (int x = xMin; x <= xMax; ++x)
    				{
    					for (int z = zMin; z <= zMax; ++z)
    					{
    						gridOccupied[z * width + x] = 1;
    						gridInfo.SetPixel(x, z, Color.black);
    					}
    				}
    			}
    		}
            // Remember to apply changes to the texture
    		gridInfo.Apply();
            // Create a new sprite with the texture & set Pixel Per Unit to the inverse of grid size. To see this, imagine that when we set the grid size to 0.5, we should render exactly 2 pixels of the texture in 1 Unity unit (remember it's a unit of length).
    		Sprite gridSprite = Sprite.Create(gridInfo, new Rect(0.0f, 0.0f, gridInfo.width, gridInfo.height), new Vector2(0.5f, 0.5f), 1f / gridSize);
    		// Now set the sprite for the image
            gridDisplay.sprite = gridSprite;
    	}
```

- ref: 
    - Change rect of an object: https://forum.unity.com/threads/modify-the-width-and-height-of-recttransform.270993/#post-4053235 
    - Texture creating & filling: https://forum.unity.com/threads/solved-changing-the-texture-of-an-ui-image-using-c.476064/
    - Find objects of type: https://docs.unity3d.com/ScriptReference/Object.FindObjectsOfType.html
    - Sprite creating: https://docs.unity3d.com/ScriptReference/Sprite.Create.html

## References

\[1] [https://blog.csdn.net/qq\_33337811/article/details/62042218](https://blog.csdn.net/qq\_33337811/article/details/62042218)

\[2] [https://stackoverflow.com/questions/48875798/add-reference-is-missing-in-visual-studio-when-using-with-unity-3d-need-npgsql](https://stackoverflow.com/questions/48875798/add-reference-is-missing-in-visual-studio-when-using-with-unity-3d-need-npgsql)

\[3] [https://developercommunity.visualstudio.com/t/project-properties-cant-be-opened-for-unity-projec/13766](https://developercommunity.visualstudio.com/t/project-properties-cant-be-opened-for-unity-projec/13766)

\[4] [https://answers.unity.com/questions/33552/gameobjectparent.html](https://answers.unity.com/questions/33552/gameobjectparent.html)

\[5] [https://forum.unity.com/threads/how-do-i-make-unity-rotate-a-scene-around-selection.77209/](https://forum.unity.com/threads/how-do-i-make-unity-rotate-a-scene-around-selection.77209/)
