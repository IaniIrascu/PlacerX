
# PlacerX

PlacerX is a geospatial application designed to collect, process, and visualize location-based data for different cities (e.g. Bucharest, New York, Paris). It aggregates data from external services (such as Google Maps via Python scripts), uses AI and Machine Learning to identify the best places for new locations for your business and then renders the information on an interactive map using Leaflet along with several plugins for enhanced visualization.

**Functionalities**

**Use of AI**

1.  **Clustering with KMeans:**
    
    -   The project uses the KMeans algorithm (from scikit-learn) to group locations based on their geographic coordinates (latitude and longitude).
    -   Clustering helps identify natural groupings among existing stores or districts, which can inform decisions about where to add new outlets.
    -   Metrics like the silhouette score are computed to evaluate the quality of the clusters, ensuring that the clusters formed are well separated.
2.  **Spatial Distance Calculations:**
    
    -   The code leverages geodesic distance computations (using geopy and scipy’s spatial functions) to measure the distances between stores and districts accurately.
    -   These calculations support functions that determine if stores fall within a certain radius of each other, which is crucial for avoiding market saturation and ensuring optimal coverage.
3.  **Data-Driven Decision Making:**
    
    -   By combining information such as income, density, and traffic with clustering results, the system performs a form of AI-assisted decision making. This helps in selecting promising locations for potential new stores by balancing proximity with economic and demographic factors.

**Integration with the rest of the project**

1.  **Data Collection and Processing**
    
    -   Python scripts (e.g. in Bucharest/script.py) query location data (using the Google Maps API) to retrieve information about various places and then store the results in CSV files (like  `department_initial.csv`,  `convenience_initial.csv`, etc.).
    -   These CSV files serve as the backend data source for the mapping interface.
2.  **Interactive Mapping Interface**
    
    -   The user interface is built in  index.html  and leverages the Leaflet library for rendering maps.
    -   The project supports multiple city datasets, with GeoJSON (or similar) scripts loaded for each city (e.g., files in the Bucharest, NewYork, and Paris folders).
3.  **Enhanced Map Visualizations**
    
    -   **3D Buildings and Advanced Rendering:**  
        The  OSMBuildings-Leaflet.js  module integrates OSMBuildings capabilities to render building facades, roofs, and shadows on the map.
    -   **Heatmap Overlays:**  
        The inclusion of the  leaflet-heat.js  provides heatmap functionality to visualize density or distribution patterns of the location data.
4.  **Spatial and Styling Functions**
    
    -   The  qgis2web_expressions.js  file defines a variety of functions (e.g. for string manipulation, geometric calculations, and conditionals) that can be used for expression-based styling and data processing on the client side, mimicking some QGIS features.
5.  **Additional UI Enhancements**
    
    -   Several Leaflet plugins are integrated (e.g. rotated markers, pattern fills, spatial indexing via RBush) to improve the user experience and provide advanced map interactions.
    -   These plugins are referenced in the HTML file (see ui/index.html) and complement the overall map rendering and data presentation.

This modular design allows for both robust backend data processing and dynamic, rich client-side mapping with multiple layers of spatial analysis and visualization.
