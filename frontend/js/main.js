document.addEventListener('DOMContentLoaded', () => {
    const previewTabs = document.querySelectorAll('.preview-tab');
    const previewPanels = document.querySelectorAll('.preview-panel');

    previewTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            previewTabs.forEach(t => t.classList.remove('active'));
            previewPanels.forEach(panel => panel.classList.remove('active'));

            tab.classList.add('active');
            const target = tab.getAttribute('data-target');
            const panel = document.getElementById(target);
            if (panel) panel.classList.add('active');
        });
    });
});

