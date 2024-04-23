import { MAP_VALIDATOR } from '@modelEntities/map';
import { createOverviewsFolder, generatingMapOverview } from '@src/backendTasks/generatingMapOverview';
import { readProjectFolder } from '@src/backendTasks/readProjectData';
import { StudioSettings } from '@utils/settings';
import { IpcMainEvent } from 'electron';
import path from 'path';

export const generatingMapOverviews = async (_: IpcMainEvent, projectPath: string, studioSettings?: StudioSettings) => {
  const maps = await readProjectFolder(projectPath, 'maps');
  const tiledOverviewPath = await createOverviewsFolder(projectPath);

  if (!studioSettings?.tiledPath) return;

  await maps.reduce(async (lastPromise, map) => {
    await lastPromise;
    const mapParsed = MAP_VALIDATOR.safeParse(JSON.parse(map));
    if (mapParsed.success && mapParsed.data.tiledFilename) {
      const mapPath = path.join(projectPath, 'Data/Tiled/Maps', `${mapParsed.data.tiledFilename}.tmx`);
      await generatingMapOverview(mapPath, tiledOverviewPath, studioSettings.tiledPath);
    }
  }, Promise.resolve());
};