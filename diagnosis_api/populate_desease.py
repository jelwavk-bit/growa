import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tomato_backend.settings')
django.setup()

from diagnosis_api.models import DiseaseInfo

def populate_data():
    data = [
        {
            "label": "Tomato___Bacterial_spot",
            "display_name": "Bacterial Spot",
            "description": "Bacterial Spot is a highly contagious disease caused by Xanthomonas bacteria. It spreads quickly in warm, rainy weather and can ruin both the appearance and the health of your tomato crop.",
            "symptoms": "You will first notice tiny, dark, water-soaked spots on the older leaves. As the infection grows, these spots develop a distinct yellow ring or 'halo' around them. If left untreated, the centers of the spots may fall out, leaving the leaves looking tattered, and eventually, the entire leaf will turn yellow and drop off.",
            "solutions": "To manage this, start by removing all infected leaves and disposing of them far away from your garden. You should apply a copper-based fungicide every 7 to 10 days, especially after it rains. It is very important to avoid touching or pruning your plants while the leaves are wet, as this is how the bacteria hitches a ride to healthy plants.",
            "preventive_measures": "Always buy certified disease-free seeds and avoid planting tomatoes in the same spot for at least three years. Space your plants widely to allow wind to dry the leaves quickly, and always aim your water at the soil, never the foliage."
        },
        {
            "label": "Tomato___Early_blight",
            "display_name": "Early Blight",
            "description": "Early Blight is a common fungal issue that usually starts at the bottom of the plant. It is often triggered by heavy dew or frequent rainfall and can lead to significant leaf loss if ignored.",
            "symptoms": "Look for brown, circular spots on the lower, older leaves near the ground. A key sign of Early Blight is the 'target' pattern—concentric rings that look like a bullseye inside the spots. Over time, the area around these spots turns yellow, and the leaf eventually dies, leaving the fruit vulnerable to sun damage.",
            "solutions": "The best first step is to prune the lower branches to improve airflow and keep leaves away from the soil. You can apply fungicides containing chlorothalonil or copper. Mulching the base of your plants with straw or plastic is also highly effective at stopping soil spores from splashing up during rain.",
            "preventive_measures": "Practice crop rotation and keep your soil healthy with compost, as strong plants resist fungus better. At the end of the season, remove all old tomato vines so the fungus doesn't hide in your soil during the winter."
        },
        {
            "label": "Tomato___Late_blight",
            "display_name": "Late Blight",
            "description": "Late Blight is one of the most dangerous tomato diseases. It moves incredibly fast in cool, wet conditions and can kill an entire healthy plant in just a few days if you don't act immediately.",
            "symptoms": "You will see large, dark, oily-looking patches appearing on the leaves and stems. During humid mornings, you might even see a white, fuzzy mold growing on the underside of these patches. The fruit will develop firm, dark brown spots that eventually rot the entire tomato.",
            "solutions": "Because this disease spreads so fast, you must pull out and destroy any plants that are heavily infected immediately to save the rest of your garden. For plants that are just starting to show spots, apply a strong fungicide like chlorothalonil or copper spray every 5 days until the weather dries up.",
            "preventive_measures": "Avoid overhead watering and ensure your garden has excellent drainage. Planting resistant varieties is the best way to prevent this 'crop killer' from taking over your farm."
        },
        {
            "label": "Tomato___Leaf_mold",
            "display_name": "Leaf Mold",
            "description": "Leaf Mold is a fungal disease that thrives in very high humidity. It is most common in greenhouses or gardens where plants are crowded too closely together.",
            "symptoms": "The first sign is pale green or yellow spots on the top of the leaves. If you flip the leaf over, you will see a dense, velvet-like coating of olive-green or purple mold. As it gets worse, the leaves will wither and drop, which prevents the fruit from growing to full size.",
            "solutions": "The most effective treatment is to increase the airflow around your plants by pruning and thinning out the branches. If the humidity stays high, you can use sulfur-based fungicides to protect the remaining healthy leaves.",
            "preventive_measures": "Keep your garden weed-free to improve air movement and avoid planting in low-lying areas where moisture gets trapped. Using a drip irrigation system will keep the leaves dry and prevent the mold from starting."
        },
        {
            "label": "Tomato___Septoria_leaf_spot",
            "display_name": "Septoria Leaf Spot",
            "description": "Septoria is a fungal infection that focuses entirely on the leaves. While it doesn't usually rot the fruit directly, it kills so many leaves that the plant loses its energy and the fruit gets sunburned.",
            "symptoms": "You will see many small, circular spots with dark borders and grey or tan centers. Inside these tiny spots, you might see small black dots that look like grains of pepper. It usually starts on the bottom leaves and slowly climbs up the plant until it looks bare.",
            "solutions": "Remove the infected lower leaves as soon as you see the spots. Apply a copper or potassium bicarbonate fungicide to the rest of the plant. Since the fungus lives in the soil, applying a fresh layer of mulch can help block the spores from reaching the leaves.",
            "preventive_measures": "Rotate your crops so you aren't planting tomatoes or peppers in the same spot every year. Watering in the morning allows the sun to dry the leaves quickly, which stops the fungus from growing."
        },
        {
            "label": "Tomato___Spider_mites_Two-spotted_spider_mite",
            "display_name": "Two-Spotted Spider Mites",
            "description": "These are tiny pests that suck the life out of the plant. They are very hard to see with the naked eye and thrive in hot, dry weather where they multiply rapidly.",
            "symptoms": "The leaves will look 'stippled' with tiny yellow or white dots. If the infestation is heavy, you will see very fine, silk-like webs covering the leaves and stems. The plant will eventually look dusty or bronzed, and the leaves will dry up and crumble.",
            "solutions": "You can blast the mites off the plants with a strong stream of water from your hose. For larger problems, use insecticidal soap or Neem oil, making sure to spray the undersides of the leaves where the mites hide.",
            "preventive_measures": "Keep your plants well-watered, as stressed and thirsty plants are much more attractive to spider mites. Encouraging ladybugs and other predatory insects in your garden can provide a natural defense."
        },
        {
            "label": "Tomato___Target_Spot",
            "display_name": "Target Spot",
            "description": "Target Spot is a fungal disease that creates very distinctive markings. It loves high humidity and warm temperatures and can affect the leaves, stems, and the fruit itself.",
            "symptoms": "The leaves develop brown spots that have clear, ring-like patterns inside them, making them look like a target. As the disease spreads, these spots grow together and turn the entire leaf brown. On the fruit, you might see circular, sunken pits that make the tomato inedible.",
            "solutions": "Apply fungicides that contain azoxystrobin or chlorothalonil. It is vital to prune the center of the plant to make sure sunlight and air can reach every branch, which helps keep the plant dry and less inviting for the fungus.",
            "preventive_measures": "Don't plant tomatoes near old debris from last year's crop. Ensure your plants are staked or caged properly so they aren't trailing on the ground where the fungus lives."
        },
        {
            "label": "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
            "display_name": "Yellow Leaf Curl Virus",
            "description": "This is a serious virus transmitted by tiny insects called whiteflies. Once a plant is infected with a virus, it cannot be cured, so prevention is the only real solution.",
            "symptoms": "New leaves will be significantly smaller than usual and will curl upward and inward. The leaves will also turn a bright, sickly yellow, especially along the edges. The whole plant will stop growing and look stunted, and it will likely stop producing any new fruit.",
            "solutions": "There is no chemical cure for the virus itself, so you must remove the infected plant immediately to prevent whiteflies from carrying the virus to your healthy plants. Focus your energy on controlling the whiteflies using yellow sticky traps and Neem oil.",
            "preventive_measures": "Use reflective silver mulches to confuse the whiteflies and keep them away. Covering young plants with a fine mesh 'floating row cover' can block the insects from reaching your crop entirely."
        },
        {
            "label": "Tomato___Tomato_mosaic_virus",
            "display_name": "Mosaic Virus",
            "description": "Mosaic Virus is an extremely tough virus that can survive on tools, hands, and even in the soil for a long time. It creates beautiful but deadly patterns on the leaves.",
            "symptoms": "The leaves will show a mottled pattern of light and dark green, similar to a mosaic tile. The leaves may also look 'crinkled' or narrow, sometimes looking like fern leaves. The fruit might have internal browning or weird yellow patches on the skin.",
            "solutions": "Like all viruses, there is no cure. You must pull out the infected plant and burn it or throw it in the trash—never compost it. Wash your hands and disinfect your garden tools with a bleach solution before touching any other plants.",
            "preventive_measures": "Avoid using tobacco near your plants, as the virus can be carried in cigarettes. Always buy seeds that are certified 'virus-free' and choose varieties labeled with 'TMV' resistance."
        },
        {
            "label": "Tomato___healthy",
            "display_name": "Healthy Tomato",
            "description": "Your plant is looking strong and vibrant! A healthy plant is the result of good soil, proper watering, and a watchful eye.",
            "symptoms": "The leaves are a deep, consistent green without any spots, holes, or curling. The stems are thick and upright, and the plant is producing flowers or fruit normally without any signs of stress or pests.",
            "solutions": "Since your plant is healthy, no chemical treatment is needed. Continue your current care routine and keep a close eye on the leaves once a week to catch any future problems early.",
            "preventive_measures": "Keep the soil consistently moist but not soggy. Apply a balanced organic fertilizer every few weeks to keep the plant's immune system strong, and keep the garden free of weeds that might hide pests."
        }
    ]

    for item in data:
        obj, created = DiseaseInfo.objects.update_or_create(
            label=item['label'],
            defaults={
                'display_name': item['display_name'],
                'description': item['description'],
                'symptoms': item['symptoms'],
                'solutions': item['solutions'],
                'preventive_measures': item['preventive_measures']
            }
        )
        if created:
            print(f"Created: {item['display_name']}")
        else:
            print(f"Updated: {item['display_name']}")

if __name__ == "__main__":
    populate_data()