# -*- coding: utf-8 -*-
path = r'E:\Desktop_E\Plugins\GitQuery\Git_Save-Load\views\git.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find where ghCard is currently (it should be between a closing div and 右键菜单)
gh_start = content.find('<div class="card" id="ghCard">')
if gh_start < 0:
    print('ERROR: ghCard not found')
    exit()

# Find ghCard end (before 右键菜单)
gh_end = content.find('\n\n<!-- \u53f3\u952e\u83dc\u5355 -->', gh_start)
if gh_end < 0:
    gh_end = content.find('\n\n<!-- 右键菜单', gh_start)

gh_section = content[gh_start:gh_end]
print(f'ghCard section: {len(gh_section)} chars')

# Remove ghCard from its current position
content = content[:gh_start] + content[gh_end:]

# Insert ghCard inside panelsArea, right before panelsArea closing
panels_close = content.find('</div><!-- end panelsArea -->')
if panels_close < 0:
    print('ERROR: panelsArea end not found')
    exit()

content = content[:panels_close] + '\n' + gh_section + '\n' + content[panels_close:]

# Remove the JS code that moves ghCard via JS (no longer needed)
old_js = '''  // ghCard \u5728 panelsArea \u5916\u90e8\uff0c\u7528 JS \u79fb\u5165\u4ee5\u4fbf\u53c2\u4e0e\u62d6\u62fd\u6392\u5e8f
  var ghCard = document.getElementById("ghCard");
  if (ghCard && ghCard.parentElement !== container) {
    container.appendChild(ghCard);
    // \u91cd\u65b0\u66f4\u65b0 draggable + \u628a\u624b
    ghCard.draggable = true;
    var ghHdr = ghCard.querySelector(".card-title");
    if (ghHdr && !ghHdr.querySelector(".drag-handle")) {
      var ghHandle = document.createElement("span");
      ghHandle.className = "drag-handle";
      ghHandle.textContent = "\u2630";
      ghHandle.style.cssText = "cursor:grab;color:var(--hana-fg-subtle,#62666d);font-size:11px;flex-shrink:0;user-select:none;margin-right:4px";
      ghHdr.insertBefore(ghHandle, ghHdr.firstChild);
    }
  }'''

if old_js in content:
    content = content.replace(old_js, '')
    print('Removed JS ghCard move code')
else:
    print('JS move code not found')
    # Try to find partial match
    idx = content.find('ghCard')
    if idx > 0:
        print(f'Found ghCard reference at {idx}: {repr(content[idx:idx+50])}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
