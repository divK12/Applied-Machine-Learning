# 🧠 Human Face Image Generation & Completion

Applied ML Final Project  
**Contributors**: Ananya Sinha, Ankita, Divyanshi Kumari, Rohit Roy

---

## 🚀 Overview

This project uses Deep Convolutional GANs (DCGANs) to:
- Generate realistic human face images.
- Complete masked regions (e.g., mouth/nose) using contextual and perceptual losses.

---

## 📂 Dataset

**CelebA Dataset**  
- 202,599 RGB images (80×80 px)
- Filtered 91k+ straight-facing images
- Applied 30×30 pixel mask near mouth region

---

## 🧠 Model Architecture

**Generator**:  
- Input: 100-dim noise  
- Layers: Dense → Upsampling → Convs → `tanh`

**Discriminator**:  
- Convs → MaxPooling → Dense → `sigmoid`

---

## 🛠 Methodology

1. Mask part of the face.
2. Optimize latent vector to minimize combined loss:
   - Contextual (pixel match)
   - Perceptual (realism via discriminator)
3. Merge generated and original pixels.

---

## 📉 Results

- Best results at 9 epochs.
- Small masks (30×30): realistic outputs.
- Large masks (40×40): loss of detail.
- More iterations = better tone but worse structure.

---

## ⚠️ Challenges

- Training instability (common in GANs)
- Sensitive to architecture tweaks
- `tanh` activation worked best

---

## 🔮 Future Work

- Use advanced models like StyleGAN
- Irregular/flexible masking
- Better preprocessing & transfer learning

---

## 📎 Links

- [CelebA Dataset](https://www.kaggle.com/datasets/jessicali9530/celeba-dataset)
- [Gamma App Presentation](https://gamma.app/?utm_source=made-with-gamma)
