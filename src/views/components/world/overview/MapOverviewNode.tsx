import { ResourceImage } from '@components/ResourceImage';
import React from 'react';
import styled from 'styled-components';
import { MapDialogsRef } from '../map/editors/MapEditorOverlay';
import { useOpenTiled } from '@utils/useOpenTiled';
import { StudioMap } from '@modelEntities/map';
import { getMapOverviewPath } from '@utils/resourcePath';
import { getSetting } from '@utils/settings';

const MapOverviewNodeContainer = styled.div`
  // Maps can be completely transparent, so we set the background color so that they are visible.
  background-color: black;
`;

type MapOverviewNodeProps = {
  data: {
    map: StudioMap;
    version: number;
    dialogsRef: MapDialogsRef;
  };
};

export const MapOverviewNode = ({ data }: MapOverviewNodeProps) => {
  const openTiled = useOpenTiled();
  const map = data.map;

  return (
    <MapOverviewNodeContainer onDoubleClick={() => getSetting('tiledPath') && openTiled(map.tiledFilename, data.dialogsRef)}>
      <ResourceImage imagePathInProject={getMapOverviewPath(map.tiledFilename)} versionId={map.mtime + data.version} />
    </MapOverviewNodeContainer>
  );
};
