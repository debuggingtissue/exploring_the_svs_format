import openslide

image = openslide.OpenSlide("TCGA-V1-A8MU-01Z-00-DX1.2C9CED13-5C2C-4FFB-AB0B-3904BAA4FEFF.svs")
print(openslide.OpenSlide.detect_format("TCGA-V1-A8MU-01Z-00-DX1.2C9CED13-5C2C-4FFB-AB0B-3904BAA4FEFF.svs"))

print(image.level_count)
print(image.dimensions)
print(image.level_dimensions)
print(image.level_downsamples)

print(image.associated_images)
image.associated_images["label"].show()
image.associated_images["macro"].show()
image.associated_images["thumbnail"].show()
