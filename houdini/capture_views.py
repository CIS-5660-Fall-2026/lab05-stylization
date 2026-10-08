"""Export one-frame flipbooks from the active Houdini Scene Viewer.

Run this inside Houdini's Python Shell after opening lab05_grammars.hipnc.
The images come directly from native L-System geometry in the viewport.
"""
import json
from pathlib import Path
import hou

ROOT=Path(__file__).resolve().parents[1]


def capture_views():
    root=hou.node('/obj/lab05_grammars')
    if root is None:
        raise RuntimeError('Open lab05_grammars.hipnc first.')
    viewer=hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
    if viewer is None:
        raise RuntimeError('A Scene View pane must be open.')
    viewer.setPwd(root)
    viewport=viewer.curViewport()
    viewport.changeType(hou.geometryViewportType.Front)
    view_settings=viewport.settings()
    for guide in (hou.viewportGuide.XYPlane,hou.viewportGuide.XZPlane,
                  hou.viewportGuide.YZPlane,hou.viewportGuide.OriginGnomon,
                  hou.viewportGuide.FloatingGnomon):
        view_settings.enableGuide(guide,False)
    config=json.loads((ROOT/'grammars/settings.json').read_text())
    out=ROOT/'images/houdini'
    out.mkdir(exist_ok=True)
    for key, model in config.items():
        for generation in model['generations']:
            node=root.node(f'{key}_n{generation:02d}')
            node.parm('numrules').set(3 if key=='fern' else 1)
            node.parm('rulefile').set('')
            node.setDisplayFlag(True)
            node.setRenderFlag(True)
            node.setCurrent(True,clear_all_selected=True)
            node.cook(force=True)
            if node.errors():
                raise RuntimeError(str(node.errors()))
            bbox=(root.node('fern_n12') if key=='fern' else node).geometry().boundingBox()
            viewport.frameBoundingBox(bbox)
            # Keep a margin when the capture aspect differs from the viewport.
            viewport.defaultCamera().setOrthoWidth(max(bbox.sizevec()[0],bbox.sizevec()[1]*1.4)*1.18)
            settings=viewer.flipbookSettings().stash()
            settings.frameRange((1,1))
            settings.outputToMPlay(False)
            settings.useResolution(True)
            settings.resolution((1400,1000))
            settings.outputZoom(100)
            settings.beautyPassOnly(True)
            settings.cropOutMaskOverlay(False)
            settings.output(str(out/f'{key}-n{generation:02d}.jpg'))
            viewer.flipbook(viewport,settings)
            print('Captured',key,generation)
    hou.hipFile.save(str(ROOT/'lab05_grammars.hipnc'))
    print('NATIVE VIEWPORT CAPTURES COMPLETE')

if __name__=='__main__':
    capture_views()
