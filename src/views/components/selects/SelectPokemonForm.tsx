import React, { useCallback, useMemo } from 'react';
import { TFunction, useTranslation } from 'react-i18next';
import { useGlobalState } from '@src/GlobalStateProvider';
import { StudioCreatureForm } from '@modelEntities/creature';
import { StudioDropDown } from '@components/StudioDropDown';
import { SelectContainerWithLabel } from './SelectContainerWithLabel';
import { BreakableSpan } from './SelectPokemon';
import { Select } from '@ds/Select';

const getFormOptions = (t: TFunction<'database_pokemon'>, forms: StudioCreatureForm[]) =>
  forms.map((formData) => ({ value: formData.form.toString(), label: t('form#') + formData.form }));

type SelectPokemonFormProps = {
  dbSymbol: string;
  form: number | string;
  onChange: (form: string) => void;
  undefValueOption?: string;
  breakpoint?: string;
  noLabel?: boolean;
};

export const SelectPokemonForm = ({ dbSymbol, form, onChange, noLabel, breakpoint, undefValueOption }: SelectPokemonFormProps) => {
  const { t } = useTranslation('database_pokemon');
  const [state] = useGlobalState();
  const options = useMemo(() => {
    const formOptions = getFormOptions(t, state.projectData.pokemon[dbSymbol]?.forms || []);
    if (undefValueOption) return [{ value: '__undef__', label: undefValueOption }, ...formOptions];
    return formOptions;
  }, [dbSymbol, undefValueOption, form, state]);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  const optionals = useMemo(() => ({ deletedOption: t('form_deleted') }), []);

  if (noLabel) return <StudioDropDown value={form.toString()} options={options} onChange={onChange} optionals={optionals} />;

  return (
    <SelectContainerWithLabel>
      <BreakableSpan breakpoint={breakpoint}>{t('form')}</BreakableSpan>
      <StudioDropDown value={form.toString()} options={options} onChange={onChange} optionals={optionals} />
    </SelectContainerWithLabel>
  );
};

type SelectCreatureFormProps = {
  name: string;
  dbSymbol: string;
  defaultValue?: string;
  onChange?: (v: string, isValid: boolean) => void;
};

export const SelectCreatureForm = ({ dbSymbol, onChange, ...props }: SelectCreatureFormProps) => {
  const { t } = useTranslation('database_pokemon');
  const [state] = useGlobalState();
  const options = useMemo(() => getFormOptions(t, state.projectData.pokemon[dbSymbol]?.forms || []), [dbSymbol, state]);
  const onValidatedChange = useCallback(
    (v: string) => {
      if (!onChange) return;

      const isValid = options.some(({ value }) => v === value);
      onChange(v, isValid);
    },
    [options, onChange]
  );

  return (
    <Select
      options={options}
      notFoundLabel={t('form_deleted')}
      chooseValue="__undef__"
      data-input-type="number"
      onChange={onValidatedChange}
      {...props}
    />
  );
};
