# Known Issues & Solutions

## Stability AI - Insufficient Credits (402 Error)

### Issue
When running the `/dang-bai` skill or `post_article.py`, the image generation fails with:
```
402 - {"errors":["You lack sufficient credits to make this request..."]
```

### Cause
The Stability AI account has run out of free credits for image generation.

### Solution
1. Go to [Stability AI Credits](https://platform.stability.ai/account/credits)
2. Purchase more credits
3. Or switch to a free image provider (Unsplash, Pexels, Pixabay via API)

### Impact
- ❌ Featured image won't be generated
- ❌ Embedded images won't be generated
- ✅ Post will still be created and published
- ✅ You can manually add images after posting

### Workaround (Temporary)
Posts can be created without images. You can:
1. Post without images using the current script
2. Manually upload images from WordPress dashboard later
3. Or wait until credits are added to the account

---

## Future Improvements

Possible enhancements if needed:
1. Add fallback to free image APIs (Unsplash, Pixabay)
2. Use Replicate.com (limited free tier: 1/hour)
3. Add option to upload manual images
4. Skip image generation with `--no-images` flag
