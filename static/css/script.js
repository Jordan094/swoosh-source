var searchCriteria = "all"; // Example value, replace with actual value from your application
    
// Function to set the collection title based on the search criteria
function setCollectionTitle(searchCriteria) {
    var collectionTitleElement = document.getElementById("collectionTitle");

    if (searchCriteria === "all") {
        collectionTitleElement.textContent = "The whole collection";
    } else if (searchCriteria === "price") {
        collectionTitleElement.textContent = "By Price";
    } else {
        // Add more conditions as needed
        collectionTitleElement.textContent = "Default Title";
    }
}