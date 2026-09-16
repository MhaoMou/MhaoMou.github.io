'use client';

import { useEffect, useRef, useState } from 'react';
import { ExternalLink } from 'lucide-react';

const games = [
  { title: 'Red Dead Redemption', cover: '/rdr1-cover.jpg', url: 'https://www.rockstargames.com/reddeadredemption/' },
  { title: 'Red Dead Redemption 2', cover: '/rdr2-cover.jpg', url: 'https://www.rockstargames.com/reddeadredemption2/' },
];

export default function EnjoyingShelf() {
  const host = useRef<HTMLDivElement>(null);
  const [rendered, setRendered] = useState(false);

  useEffect(() => {
    const element = host.current;
    if (!element) return;
    let disposed = false;
    let cleanup = () => {};
    void import('three').then(THREE => {
      if (disposed) return;
      let renderer: import('three').WebGLRenderer;
      try { renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, preserveDrawingBuffer: true }); }
      catch { return; }
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer.shadowMap.enabled = true;
      renderer.shadowMap.type = THREE.PCFSoftShadowMap;
      renderer.outputColorSpace = THREE.SRGBColorSpace;
      renderer.domElement.setAttribute('aria-hidden', 'true');
      renderer.domElement.style.width = '100%';
      renderer.domElement.style.height = '100%';
      element.appendChild(renderer.domElement);
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(35, 1, 0.1, 50);
      camera.position.set(0.35, 2.4, 7.5);
      camera.lookAt(0, 0.65, 0);
      scene.add(new THREE.HemisphereLight(0xffffff, 0x80918a, 2.6));
      const light = new THREE.DirectionalLight(0xffffff, 4);
      light.position.set(-3, 6, 5);
      light.castShadow = true;
      light.shadow.mapSize.set(1024, 1024);
      scene.add(light);

      const objects: import('three').Mesh[] = [];
      function box(width: number, height: number, depth: number, color: number, x: number, y: number, z: number) {
        const mesh = new THREE.Mesh(new THREE.BoxGeometry(width, height, depth), new THREE.MeshStandardMaterial({ color, roughness: 0.75 }));
        mesh.position.set(x, y, z);
        mesh.castShadow = true;
        mesh.receiveShadow = true;
        objects.push(mesh);
        return mesh;
      }
      const shelf = box(5.2, 0.17, 1.15, 0xa37650, 0, 0, 0);
      scene.add(shelf);
      const grain = document.createElement('canvas');
      grain.width = 512; grain.height = 64;
      const context = grain.getContext('2d');
      let wood: import('three').CanvasTexture | undefined;
      if (context) {
        context.fillStyle = '#ae825b'; context.fillRect(0, 0, 512, 64);
        for (let row = 0; row < 64; row += 2) {
          context.strokeStyle = row % 6 ? '#a37650' : '#bd9671';
          context.beginPath(); context.moveTo(0, row);
          for (let x = 0; x <= 512; x += 16) context.lineTo(x, row + Math.sin(x / 55 + row) * 1.5);
          context.stroke();
        }
        wood = new THREE.CanvasTexture(grain); wood.colorSpace = THREE.SRGBColorSpace;
        (shelf.material as import('three').MeshStandardMaterial).map = wood;
      }
      [-1.8, 1.8].forEach(x => {
        scene.add(box(0.09, 0.45, 0.55, 0x424b49, x, -0.3, -0.2));
      });
      const covers: import('three').Texture[] = [];
      let loaded = 0;
      const loader = new THREE.TextureLoader();
      const cases = games.map((item, index) => {
      const game = new THREE.Group();
      game.position.set(index === 0 ? -0.95 : 0.95, 1.19, 0.12);
      game.rotation.y = -0.16;
      game.add(box(1.48, 2.2, 0.2, 0x22262a, 0, 0, 0));
      const cover = new THREE.Mesh(new THREE.PlaneGeometry(1.4, 2.1), new THREE.MeshStandardMaterial({ color: 0xb71920, roughness: 0.6 }));
      cover.position.z = 0.105;
      game.add(cover); objects.push(cover);
      scene.add(game);
      loader.load(item.cover, texture => {
        if (disposed) { texture.dispose(); return; }
        covers.push(texture);
        texture.colorSpace = THREE.SRGBColorSpace;
        texture.anisotropy = renderer.capabilities.getMaxAnisotropy();
        (cover.material as import('three').MeshStandardMaterial).map = texture;
        (cover.material as import('three').MeshStandardMaterial).color.set(0xffffff);
        (cover.material as import('three').MeshStandardMaterial).needsUpdate = true;
        loaded += 1;
        if (loaded === games.length) setRendered(true);
      });
      return game;
      });
      let desiredRotation = -0.16;
      const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
      const move = (event: PointerEvent) => {
        if (reduced.matches) return;
        const rect = element.getBoundingClientRect();
        desiredRotation = -0.16 + ((event.clientX - rect.left) / rect.width - 0.5) * 0.65;
      };
      const leave = () => { desiredRotation = -0.16; };
      element.addEventListener('pointermove', move);
      element.addEventListener('pointerleave', leave);
      const resize = () => {
        const width = element.clientWidth;
        const height = element.clientHeight;
        renderer.setSize(width, height, false);
        camera.aspect = width / height;
        camera.position.z = camera.aspect < 1.3 ? 9.6 : 7.5;
        camera.updateProjectionMatrix();
      };
      const observer = new ResizeObserver(resize); observer.observe(element); resize();
      renderer.setAnimationLoop(() => {
        cases.forEach(game => { game.rotation.y += (desiredRotation - game.rotation.y) * 0.08; });
        renderer.render(scene, camera);
      });
      cleanup = () => {
        observer.disconnect();
        element.removeEventListener('pointermove', move); element.removeEventListener('pointerleave', leave);
        renderer.setAnimationLoop(null);
        objects.forEach(mesh => { mesh.geometry.dispose(); (mesh.material as import('three').Material).dispose(); });
        wood?.dispose(); covers.forEach(texture => texture.dispose()); renderer.dispose(); renderer.domElement.remove();
      };
    }).catch(() => { /* Keep the cover fallback when WebGL cannot initialize. */ });
    return () => { disposed = true; cleanup(); };
  }, []);

  return (
    <section id="enjoying" className="border-t border-neutral-200 pt-8">
      <h2 className="text-2xl font-serif font-bold text-primary">Currently enjoying</h2>
      <div ref={host} role="img" aria-label="A wooden 3D shelf holding Red Dead Redemption and Red Dead Redemption 2 game cases" className="relative h-[300px] sm:h-[360px] w-full">
        {!rendered && <div className="absolute inset-0 flex gap-6 items-center justify-center pointer-events-none">
          {games.map(item => (
          // eslint-disable-next-line @next/next/no-img-element
          <img key={item.title} src={item.cover} alt={`${item.title} cover`} width={140} height={210} className="h-[180px] w-[120px] sm:h-[210px] sm:w-[140px] object-cover shadow-xl" />
          ))}
        </div>}
      </div>
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {games.map(item => <div key={item.title}>
          <h3 className="font-medium">{item.title}</h3>
          <a href={item.url} target="_blank" rel="noopener noreferrer" className="mt-1 inline-flex items-center gap-1.5 text-sm text-neutral-500 hover:text-primary">Rockstar Games<ExternalLink size={14} /></a>
        </div>)}
      </div>
    </section>
  );
}
