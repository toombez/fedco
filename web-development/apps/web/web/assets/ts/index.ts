function initDrawer() {
    const $drawer = document.querySelector('[data-drawer]')
    const $drawerToggle = document.querySelector('[data-drawer-toggle]')

    if (!$drawer) {
        throw new Error('cannot find drawer')
    }
    if (!$drawerToggle) {
        throw new Error('cannot find drawer toggle button')
    }

    $drawerToggle.addEventListener('click', () => {
        $drawer.classList.toggle('hidden')
    })

    document.addEventListener('click', (event) => {
        if ($drawerToggle.contains(event.target as Node)) {
            return
        }

        if ($drawer.contains(event.target as Node)) {
            return
        }

        $drawer.classList.add('hidden')
    })

    return {
        $drawer,
        $drawerToggle,
    }
}

initDrawer()