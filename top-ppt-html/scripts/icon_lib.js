/**
 * TopPPT HTML · 语义图标库（SVG 内容 · 24×24 · stroke 1.8）
 * 单源：与 references/icons.md / render_from_model.py ICONS 同语义。
 * build_pptx.js 用 sharp 栅格化为 PNG 后嵌入（真导出，不再用 accent 方块替代）。
 * sync_runtime.py 校验三处图标键一致。
 */
'use strict';

const SVG_OPEN = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">';

/** name → SVG 完整标记（currentColor 由调用方替换为目标色） */
const ICONS = {
  '增长': SVG_OPEN + '<path d="M22 7l-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/></svg>',
  '下降': SVG_OPEN + '<path d="M22 17l-8.5-8.5-5 5L2 7"/><path d="M16 17h6v-6"/></svg>',
  '数据': SVG_OPEN + '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4.03 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4.03 3 9 3s9-1.34 9-3"/></svg>',
  '图表': SVG_OPEN + '<path d="M3 3v18h18"/><rect x="7" y="12" width="3" height="6" rx="1"/><rect x="12" y="8" width="3" height="10" rx="1"/><rect x="17" y="4" width="3" height="14" rx="1"/></svg>',
  '趋势': SVG_OPEN + '<path d="M3 3v18h18"/><path d="M7 14l4-4 3 3 5-6"/><path d="M15 7h4v4"/></svg>',
  '占比': SVG_OPEN + '<path d="M21.2 15.9A10 10 0 1 1 8 2.8"/><path d="M22 12A10 10 0 0 0 12 2v10z"/></svg>',
  '表格': SVG_OPEN + '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18M15 3v18"/></svg>',
  '效率': SVG_OPEN + '<path d="M12 15l3.5-5.5"/><path d="M20.2 15a8.5 8.5 0 1 0-16.4 0"/></svg>',
  '成果': SVG_OPEN + '<circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/></svg>',
  '安全': SVG_OPEN + '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>',
  '权限': SVG_OPEN + '<rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
  '检查': SVG_OPEN + '<circle cx="12" cy="12" r="10"/><path d="M8 12.5l2.5 2.5L16 9.5"/></svg>',
  '风险': SVG_OPEN + '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/></svg>',
  '团队': SVG_OPEN + '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
  '流程': SVG_OPEN + '<circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M6 21V9a9 9 0 0 0 9 9"/></svg>',
  '计划': SVG_OPEN + '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
  '智能': SVG_OPEN + '<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 9h6v6H9zM9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/></svg>',
  '洞察': SVG_OPEN + '<circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>',
  '工具': SVG_OPEN + '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
  '清单': SVG_OPEN + '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/></svg>',
};

const ORDER = Object.keys(ICONS);

/** 按标题语义挑图标名；未命中按序轮换（与 render_from_model.pick_icon 同策略） */
function pickIconName(title, idx) {
  const t = String(title || '');
  for (const key of ORDER) {
    if (t.includes(key)) return key;
  }
  return ORDER[(idx || 0) % ORDER.length];
}

/** 渲染为带指定描边色的 SVG 字符串 */
function iconSvg(name, color) {
  const raw = ICONS[name] || ICONS[ORDER[0]];
  const c = color || '#1a56a8';
  return raw.replace('stroke="currentColor"', `stroke="${c}"`);
}

module.exports = { ICONS, ORDER, pickIconName, iconSvg, SVG_OPEN };
