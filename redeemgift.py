# Add this as another app or expand your collection
popup_hell_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body { background: #1e1b4b; color: white; font-family: sans-serif; text-align: center; padding-top: 100vh; height: 200vh; }
        .spawn-btn { padding: 15px 30px; background: #ec4899; color: white; border: none; font-size: 20px; font-weight: bold; border-radius: 8px; cursor: pointer; }
        .mini-popup { position: absolute; width: 220px; background: #fff; color: #333; padding: 15px; border-radius: 6px; box-shadow: 0 5px 15px rgba(0,0,0,0.3); font-size: 14px; text-align: left; z-index: 999; }
        .mini-popup button { float: right; background: #ef4444; color: white; border: none; padding: 2px 6px; cursor: pointer; border-radius: 3px; }
    </style>
</head>
<body>
    <button class="spawn-btn" onclick="startChaos()">🎁 Click Here to Claim Your Free Prize!</button>
    <script>
        function startChaos() {
            for(let i=0; i<3; i++) createPopup();
        }
        function createPopup() {
            const div = document.createElement('div');
            div.className = 'mini-popup';
            div.style.left = Math.random() * (window.innerWidth - 250) + 'px';
            div.style.top = Math.random() * (window.innerHeight - 150) + 'px';
            div.innerHTML = '⚠️ Warning: Virus Found! <button onclick="this.parentElement.remove(); startChaos();">X</button>';
            document.body.appendChild(div);
        }
    </script>
</body>
</html>
"""