import cv2
import pytesseract

# Load the image
image = cv2.imread("/assert/img/plateCar.png")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply noise reduction
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Detect contours
contours, _ = cv2.findContours(blur_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter potential license plate contours
license_plate_contours = []
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    if len(approx) == 4:  # Check if it's a quadrilateral (license plate shape)
        license_plate_contours.append(approx)

# Extract and segment characters from the best license plate contour
for contour in license_plate_contours:
    x, y, w, h = cv2.boundingRect(contour)
    plate_region = image[y : y + h, x : x + w]

    # Binarize the plate region
    ret, thresh = cv2.threshold(plate_region, 127, 255, cv2.THRESH_BINARY)

    # Apply morphological operations to separate characters
    morph = cv2.morphologyEx(
        thresh, cv2.MORPH_OPEN, kernel=cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    )

    # Extract and recognize individual characters
    characters = []
    for x, y, w, h in cv2.boundingRect(
        cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    ):
        character_region = morph[y : y + h, x : x + w]
        character = pytesseract.image_to_string(character_region, config="--psm 10")
        characters.append(character)

    # Combine characters to form the license plate number
    license_plate_number = "".join(characters)
    print("License Plate Number:", license_plate_number)

    # Display the recognized license plate
    cv2.imshow("License Plate", plate_region)
    cv2.waitKey(0)
